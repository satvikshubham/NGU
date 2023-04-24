from pyneqsys.symbolic import SymbolicSys
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
import re


class Solution():
    def __init__(self, equations):
        self.equations = []
        self.variables = []
        self.num_variables = 0
        self.num_equations = 0
        self.setup(equations)
    
    def setup(self, equations):
        self.equations = equations
        var_pattern = re.compile(r'\b[a-zA-Z]+\b')
        variables = []
        for i in range(len(equations)):
            variables = variables + var_pattern.findall(equations[i])
        self.variables = list(set(variables))
        to_remove = ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', 'pi', 'e']
        for i in range(len(to_remove)):
            if to_remove[i] in self.variables:
                self.variables.remove(to_remove[i])
        # replace '^' with '**'
        for i in range(len(self.equations)):
            temp_len = len(self.equations[i])
            for j in range(temp_len):
                if self.equations[i][j] == '^':
                    self.equations[i] = self.equations[i][:j] + '**' + self.equations[i][j+1:]
                    temp_len += 1
        self.num_variables = len(self.variables)
        self.num_equations = len(self.equations)
    
    def eq_callback(self,_x):
        # shallow copy variables from self.variables
        variables = self.variables[:]
        for i in range(self.num_variables):
            variables[i] = _x[i]
        equations = []
        for i in range(self.num_equations):
            eqn = parse_expr(self.equations[i])
            eqn_subs = eqn.subs(variables)
            equations.append(eqn_subs)
    
        return equations
    
    def get_solution(self):
        symbolic_sys = SymbolicSys.from_callback(self.eq_callback, self.num_variables)
        x0, info = symbolic_sys.solve([1, 2])
        assert info['success']
        return x0


equations = ["(x - y)**1/2 + x - 1", "sin(x - y) + xy - 1*e^(2)"]
solutions = Solution(equations)
print(solutions.get_solution())