import time
from gekko import GEKKO
from sympy import *
import re

class Solution():
    def __init__(self):
        self.equations = []
        self.variables = []
        self.num_equations = 0

    def process_equations(self, equations):
        equations = [x.replace('=', '==') for x in equations]
        equations = [x.replace('sin', '_m.sin') for x in equations]
        equations = [x.replace('cos', '_m.cos') for x in equations]
        equations = [x.replace('tan', '_m.tan') for x in equations]
        equations = [x.replace('sqrt', '_m.sqrt') for x in equations]
        equations = [x.replace('log', '_m.log') for x in equations]
        equations = [x.replace('ln', '_m.log') for x in equations]
        equations = [x.replace('exp', '_m.exp') for x in equations]
        equations = [x.replace('pi', '_m.pi') for x in equations]
        equations = [x.replace('e', '_m.e') for x in equations]
        equations = [x.replace('E', '_m.e') for x in equations]
        return equations

    def get_variables(self, equations):
        var_pattern = re.compile(r'\b[a-zA-Z]+\w*\d*\b')
        variables = []
        for i in range(len(equations)):
            variables += var_pattern.findall(equations[i])
        self.variables = list(set(variables))
        to_remove = ['sin', 'cos', 'tan', 'sqrt',
                    'log', 'ln', 'exp', 'pi', 'e']
        for i in range(len(to_remove)):
            if to_remove[i] in self.variables:
                self.variables.remove(to_remove[i])

    def solution(self, equations, num_variables):
        equations = self.process_equations(equations)
        _m = GEKKO()
        self.get_variables(equations)
        var_names = [str(var) for var in self.variables]
        # Create variables
        exec_dict = {}
        for var_name in var_names:
            exec_dict[var_name] = _m.Var(1)
            exec(f"{var_name} = exec_dict['{var_name}']")

        # Create equations
        temp = ""
        for _x in equations:
            temp += _x + ','
        temp = temp[:-1]
        exec(f"_m.Equations([{temp}])")

        start_time = time.time()
        _m.solve(disp=False)
        end_time = time.time()
        # Retrieve variable values
        answers = [exec_dict[var].value for var in var_names]
        _d = {}
        for _ in range(len(var_names)):
            _d[var_names[_]] = answers[_]
            
        print(f"Time taken: {end_time - start_time} seconds")
        return _d
        # print(abc.value, b.value, c.value, d.value, k.value, f.value, g.value, h.value, i.value, j.value)
