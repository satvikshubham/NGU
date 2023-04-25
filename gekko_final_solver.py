import re
from sympy import *
from gekko import GEKKO
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
        
        # convert variables to symbols
        self.variables = [Symbol(i) for i in self.variables]
        for i in range (len(self.equations)):
            parse_expr(self.equations[i])
            
        self.num_variables = len(self.variables)
        self.num_equations = len(self.equations)


equations = ["(x - y)^1/2 + x == 1", "sin(x - y) + xy - 1*e^(2) == 0"]
solutions = Solution(equations)