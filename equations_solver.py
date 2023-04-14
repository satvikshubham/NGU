from pyneqsys.symbolic import SymbolicSys
from sympy.parsing.sympy_parser import parse_expr
from sympy import *


def equation_callback(expr, variables, x):
    
    return expr

def eq_callback(exprs, variables, x):
    #  Define the variables
    # x, y = x[0], x[1]
    
    # # Define the equations
    # eq1 = (x - y)**1/2 + x - 1
    # eq2 = (sin(x) - y)**2 + x - 1
    
    # # Return the equations as a list
    # return [eq1, eq2]
    
    # make generic version of the above code
    for i in range (len(variables)):
        variables[i] = x[i]
    
    # for i in range(len(exprs)):
    
    # return exprs

def get_solution(n, equations):
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
        eq_len_i = len(equations[i])
        for j in range(eq_len_i):
            if equations[i][j] == '^':
                equations[i] = equations[i][:j] + '**' + equations[i][j+1:]
                eq_len_i += 1
        parsed_equations.append(equations[i])
    
    
    # for i in range(len(equations)):
    #     # replace '^' with '**'
    #     for j in range(len(equations[i])):
    #         if equations[i][j] == '^':
    #             equations[i] = equations[i][:j] + '**' + equations[i][j+1:]
                
    #     parsed_equations.append(equation_callback(equations[i], variables, x))   
        
    print(parsed_equations)     
    return 1

neqsys = SymbolicSys.from_callback(
    lambda x: [(x[0] - x[1])**1/2 + x[0] - 1,
               (sin(x[0]) - x[1])**2 + x[0] - 1,
               ], 2)
x, info = neqsys.solve([1, 2])


assert info['success']
print(x)



equations = ["(x - y)^1/2 + x - 1", "(sin(x) - y)^2 + x - 1"]
get_solution(2, equations)