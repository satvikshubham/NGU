from sympy import Symbol, sqrt, sin
from pyneqsys.symbolic import SymbolicSys

def equation_callback(x):
    # Define the variables
    x, y = x[0], x[1]
    
    # Define the equations
    eq1 = (x - y)**1/2 + x - 1
    eq2 = (sin(x) - y)**2 + x - 1
    
    # Return the equations as a list
    return [eq1, eq2]

# Define the number of variables
num_vars = 2

# Create the SymbolicSys object
symbolic_sys = SymbolicSys.from_callback(equation_callback, num_vars)
x, info = symbolic_sys.solve([1, 2])
assert info['success']
print(x)