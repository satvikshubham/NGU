from gekko import GEKKO
import sympy
import re


class Solution():
    def __init__(self):
        self.equations = []
        self.variables = []
        # self.num_variables = num_variables
        self.num_equations = 0
        # self.get_variables(equations)
        # self.solution(equations)
        
        
    def get_variables(self, equations):
        var_pattern = re.compile(r'\b[a-zA-Z]+\b')
        variables = []
        for i in range(len(equations)):
            variables = variables + var_pattern.findall(equations[i])
        self.variables = list(set(variables))
        to_remove = ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', 'pi', 'e']
        for i in range(len(to_remove)):
            if to_remove[i] in self.variables:
                self.variables.remove(to_remove[i])
        
    def solution(self, equations, num_variables):        
        # # Create a Gekko model
        # m = GEKKO()

        # # Define the variables (assuming x and y are the only variables)
        
        # input_strings = equations
        # variable_names = []
        # for i in range(len(self.variables)):
        #     variable_names.append(str(self.variables[i]))
            
        # variables = [m.Var() for _ in range(len(variable_names))]
        # variable_dict = dict(zip(variable_names, variables))
        
        # # Convert input strings to sympy expressions
        # sympy_exprs = []
        # for eq in input_strings:
        #     try:
        #         sympy_exprs.append(sympy.sympify(eq.replace('=', '-')))
        #     except sympy.SympifyError as e:
        #         # print(f"Error: {e}")
        #         # print(f"Expression: {eq}")
        #         return None, None

        # # Define the Gekko equivalent of the sympy functions
        # gekko_functions = {
        #     sympy.sin: m.sin,
        #     sympy.cos: m.cos,
        #     sympy.tan: m.tan,
        #     sympy.exp: m.exp,
        #     sympy.log: m.log,
        #     sympy.sqrt: m.sqrt,
        # }

        # # Convert sympy expressions to Gekko expressions
        # def sympy_to_gekko(expr, variables):
        #     if expr.is_Atom:
        #         if expr.is_Symbol:
        #             return variable_dict[expr.name]
        #         else:
        #             return expr
        #     else:
        #         if expr.func in gekko_functions:
        #             gekko_func = gekko_functions[expr.func]
        #             return gekko_func(*[sympy_to_gekko(arg, variables) for arg in expr.args])
        #         elif expr.func == sympy.Pow:
        #             return m.exp(sympy_to_gekko(expr.args[1], variables) * m.log(sympy_to_gekko(expr.args[0], variables)))
        #         elif expr.func == sympy.Add:
        #             return sum([sympy_to_gekko(arg, variables) for arg in expr.args])
        #         elif expr.func == sympy.Mul:
        #             result = sympy_to_gekko(expr.args[0], variables)
        #             for arg in expr.args[1:]:
        #                 result *= sympy_to_gekko(arg, variables)
        #             return result
        #         else:
        #             try:
        #                 return expr.func(*[sympy_to_gekko(arg, variables) for arg in expr.args])
        #             except Exception as e:
        #                 print(f"Error: {e}")
        #                 print(f"Unsupported expression: {expr}")
        #                 raise


        # gekko_exprs = [sympy_to_gekko(expr, variables) for expr in sympy_exprs]

        # # Add equations to the Gekko model
        # for expr in gekko_exprs:
        #     m.Equation(expr == 0)

        # # Solve the system of equations
        # m.solve(disp=False)
        
        # # return variables, variable_dict
        # # Print the solution
        # for var in variables:
        #     print(f"{var.name}: {var.value[0]}")
        
        
        
        # m = GEKKO()

        # # Extract variable names from the input strings
        # var_names = []
        # for i in range (len(self.variables)):
        #     var_names.append(str(self.variables[i]))

        # # Define the Gekko variables
        # gekko_vars = {name: m.Var() for name in var_names}

        # # Convert input strings to sympy expressions
        # sympy_exprs = []
        # input_strings = equations
        # for eq in input_strings:
        #     try:
        #         sympy_exprs.append(sympy.sympify(eq.replace('e', 'E').replace('^', '**').replace('=', '-')))
        #     except sympy.SympifyError as e:
        #         print(f"Error: {e}")
        #         print(f"Expression: {eq}")

        # # Define the Gekko equivalent of the sympy functions
        # gekko_functions = {
        #     sympy.sin: m.sin,
        #     sympy.cos: m.cos,
        #     sympy.tan: m.tan,
        #     sympy.exp: m.exp,
        #     sympy.log: m.log,
        #     sympy.sqrt: m.sqrt,
        # }

        # # Convert sympy expressions to Gekko expressions
        # def sympy_to_gekko(expr):
        #     if expr.is_Atom:
        #         if expr.is_Symbol:
        #             return gekko_vars[expr.name]
        #         else:
        #             return expr
        #     else:
        #         if expr.func in gekko_functions:
        #             gekko_func = gekko_functions[expr.func]
        #             return gekko_func(*[sympy_to_gekko(arg) for arg in expr.args])
        #         elif expr.func == sympy.Pow:
        #             return m.exp(sympy_to_gekko(expr.args[1]) * m.log(sympy_to_gekko(expr.args[0])))
        #         elif expr.func == sympy.Add:
        #             return sum([sympy_to_gekko(arg) for arg in expr.args])
        #         elif expr.func == sympy.Mul:
        #             result = sympy_to_gekko(expr.args[0])
        #             for arg in expr.args[1:]:
        #                 result *= sympy_to_gekko(arg)
        #             return result
        #         else:
        #             try:
        #                 return expr.func(*[sympy_to_gekko(arg) for arg in expr.args])
        #             except Exception as e:
        #                 print(f"Error: {e}")
        #                 print(f"Unsupported expression: {expr}")
        #                 raise

        # gekko_exprs = [sympy_to_gekko(expr) for expr in sympy_exprs]

        # # Add equations to the Gekko model
        # for expr in gekko_exprs:
        #     m.Equation(expr == 0)

        # # Solve the system of equations
        # m.solve(disp=False)

        # # Print the solution
        # # for name, var in gekko_vars.items():
        # #     print(f"{name}: {var.value[0]}")
        # print(gekko_vars)
        
        
        m = GEKKO()
        var_names = []
        self.get_variables(equations)
        for i in range (len(self.variables)):
            var_names.append(str(self.variables[i]))
        gekko_vars = {name: m.Var() for name in var_names}
        sympy_exprs = []
        input_strings = equations
        for eq in input_strings:
            try:
                sympy_exprs.append(sympy.sympify(eq.replace('e', 'E').replace('^', '**').replace('=', '-')))
            except sympy.SympifyError as e:
                return None
        gekko_functions = {
            sympy.sin: m.sin,
            sympy.cos: m.cos,
            sympy.tan: m.tan,
            sympy.exp: m.exp,
            sympy.log: m.log,
            sympy.sqrt: m.sqrt,
        }
        def sympy_to_gekko(expr):
            if expr.is_Atom:
                if expr.is_Symbol:
                    return gekko_vars[expr.name]
                else:
                    return expr
            else:
                if expr.func in gekko_functions:
                    gekko_func = gekko_functions[expr.func]
                    return gekko_func(*[sympy_to_gekko(arg) for arg in expr.args])
                elif expr.func == sympy.Pow:
                    return m.exp(sympy_to_gekko(expr.args[1]) * m.log(sympy_to_gekko(expr.args[0])))
                elif expr.func == sympy.Add:
                    return sum([sympy_to_gekko(arg) for arg in expr.args])
                elif expr.func == sympy.Mul:
                    result = sympy_to_gekko(expr.args[0])
                    for arg in expr.args[1:]:
                        result *= sympy_to_gekko(arg)
                    return result
                else:
                    try:
                        return expr.func(*[sympy_to_gekko(arg) for arg in expr.args])
                    except Exception as e:
                        print(f"Error: {e}")
                        print(f"Unsupported expression: {expr}")
                        raise

        gekko_exprs = [sympy_to_gekko(expr) for expr in sympy_exprs]
        for expr in gekko_exprs:
            m.Equation(expr == 0)
        m.solve(disp=False)
        return gekko_vars
    
    
      
# if __main__ == "__main__":



# input_strings = ["(axbu - sinaoq)**(1/2) + axbu = 1", "sin(axbu - sinaoq) + axbu*sinaoq - exp(2) = 0"]
# # # input_strings = ["ab + bc + ca = 12", "2*bc + 3*ca = 7", "ca + bc = 4"]

# num_variables = len(input_strings)
# s = Solution(input_strings, num_variables)
