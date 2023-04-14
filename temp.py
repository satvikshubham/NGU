from pyneqsys.symbolic import SymbolicSys
from sympy.parsing.sympy_parser import parse_expr
from sympy import *


def equation_callback(expr, variables, x):
    parsed_expr = parse_expr(expr)
    
    # Define the variables
    x1, x2 = symbols(variables[0]), symbols(variables[1])
    
    # Replace variable names in the expression with the corresponding symbols
    parsed_expr = parsed_expr.subs({x1: x[0], x2: x[1]})
    
    # Return the parsed expression
    return parsed_expr


def get_solution(n, equations, x):
    # extract distinct letters from the equations and store it in a list
    variables = []
    for i in range(len(equations)):
        for j in range(len(equations[i])):
            if equations[i][j].isalpha() and equations[i][j] not in variables:
                variables.append(equations[i][j])
    # assign variables to indices 
    d = {}
    for i in range(len(variables)):
        d[variables[i]] = i
        
    parsed_equations = []
    # parse expressions from the equations
    for i in range(len(equations)):
        # replace '^' with '**'
        for j in range(len(equations[i])):
            if equations[i][j] == '^':
                equations[i] = equations[i][:j] + '**' + equations[i][j+1:]
                
        parsed_equations.append(equation_callback(equations[i], variables, x))   
        
    # Create the SymbolicSys object
    symbolic_sys = SymbolicSys.from_callback(lambda x: parsed_equations, n)
    x, info = symbolic_sys.solve([1, 0])
    
    print(x)
    assert info['success']
    return x


equations = ["x + y - 3", "x + y - 1"]
x = [5, 2]
get_solution(2, equations, x)
