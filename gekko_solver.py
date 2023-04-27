# from gekko import GEKKO
# import sympy
# import re


# class Solution():
#     def __init__(self):
#         self.equations = []
#         self.variables = []
#         self.num_equations = 0

#     def get_variables(self, equations):
#         var_pattern = re.compile(r'\b[a-zA-Z]+\b')
#         variables = []
#         for i in range(len(equations)):
#             variables = variables + var_pattern.findall(equations[i])
#         self.variables = list(set(variables))
#         to_remove = ['sin', 'cos', 'tan', 'sqrt',
#                      'log', 'ln', 'exp', 'pi', 'e']
#         for i in range(len(to_remove)):
#             if to_remove[i] in self.variables:
#                 self.variables.remove(to_remove[i])

#     def solution(self, equations, num_variables):
#         m = GEKKO()
#         m.options.SOLVER = 2
#         var_names = []
#         self.get_variables(equations)
#         for i in range(len(self.variables)):
#             var_names.append(str(self.variables[i]))
#         gekko_vars = {name: m.Var(1) for name in var_names}
#         sympy_exprs = []
#         input_strings = equations
#         for eq in input_strings:
#             try:
#                 sympy_exprs.append(sympy.sympify(eq.replace(
#                     'e', 'E').replace('^', '**').replace('=', '-')))
#             except sympy.SympifyError as e:
#                 print(eq)
#                 return None
#         gekko_functions = {
#             sympy.sin: m.sin,
#             sympy.cos: m.cos,
#             sympy.tan: m.tan,
#             sympy.exp: m.exp,
#             sympy.log: m.log,
#             sympy.sqrt: m.sqrt,
#         }

#         def sympy_to_gekko(expr):
#             if expr.is_Atom:
#                 if expr.is_Symbol:
#                     return gekko_vars[expr.name]
#                 else:
#                     return expr
#             else:
#                 if expr.func in gekko_functions:
#                     gekko_func = gekko_functions[expr.func]
#                     return gekko_func(*[sympy_to_gekko(arg) for arg in expr.args])
#                 elif expr.func == sympy.Pow:
#                     return m.exp(sympy_to_gekko(expr.args[1]) * m.log(sympy_to_gekko(expr.args[0])))
#                 elif expr.func == sympy.Add:
#                     return sum([sympy_to_gekko(arg) for arg in expr.args])
#                 elif expr.func == sympy.Mul:
#                     result = sympy_to_gekko(expr.args[0])
#                     for arg in expr.args[1:]:
#                         result *= sympy_to_gekko(arg)
#                     return result
#                 else:
#                     try:
#                         return expr.func(*[sympy_to_gekko(arg) for arg in expr.args])
#                     except Exception as e:
#                         print(f"Error: {e}")
#                         print(f"Unsupported expression: {expr}")
#                         raise

#         gekko_exprs = [sympy_to_gekko(expr) for expr in sympy_exprs]
#         print(gekko_exprs)
#         print(gekko_vars)
#         for expr in gekko_exprs:
#             m.Equation(expr == 0)
#         m.solve(disp=False)
#         return gekko_vars

# # equations = ["x**2 + y**2 = 26",
# # "3*x**2 + 25*y**2 = 100"]
# # s = Solution()
# # print(s.solution(equations, 2))

# equations = [
#     "5-(100+23*9)*abc+23*9*b-23*20*abc**2+23*20*b**2 = 0",
#     "100*abc-(100+23*9)*b+23*9*c-23*20*b**2+23*20*c**2 = 0",
#     "100*b-(100+23*9)*c+23*9*d-23*20*c**2+23*20*d**2 = 0",
#     "100*c-(100+23*9)*d+23*9*k-23*20*d**2+23*20*k**2 = 0",
#     "100*d-(100+23*9)*k+23*9*f-23*20*k**2+23*20*f**2 = 0",
#     "100*k-(100+23*9)*f+23*9*g-23*20*f**2+23*20*g**2 = 0",
#     "0.039+100*f+(-100+9*23)*g-9*10*h+20*23*g**2-20*10*h**2 = 0",
#     "100*g-(100+9*10)*h-9*10*i-20*10*h**2-20*10*i**2 = 0",
#     "100*h-(100+9*10)*i-9*10*j-20*10*i**2-20*10*j**2 = 0",
#     "100*i-(100+9*10)*j-20*10*j**2 = 0"
# ]

# s = Solution()
# print(s.solution(equations, len(equations)))


from gekko import GEKKO
from sympy import *
from varname import nameof
import re
import sympy


class Solution():
    def __init__(self):
        self.equations = []
        self.variables = []
        self.num_equations = 0

    def process_equations(self, equations):
        # replace = with ==
        equations = [x.replace('=', '==') for x in equations]
        # replace ^ with **
        equations = [x.replace('^', '**') for x in equations]
        # replace sin, cos, tan, sqrt, log, ln, exp with their respective functions
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
        var_pattern = re.compile(r'\b[a-zA-Z]+\b')
        variables = []
        for i in range(len(equations)):
            variables = variables + var_pattern.findall(equations[i])
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
        for x in equations:
            temp += x + ','
        temp = temp[:-1]
        exec(f"_m.Equations([{temp}])")

        _m.solve(disp=False)

        # Retrieve variable values
        answers = [exec_dict[var].value for var in var_names]
        _d = {}
        for _ in range(len(var_names)):
            _d[var_names[_]] = answers[_]
        return _d
