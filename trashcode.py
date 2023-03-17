
# def solve(equations, esp = 0.0001, max_iter = 100):
#     _vars, _equations, _constants = set_inputs(equations)
#     _jacobian = compute_jacobian(_equations, _vars)
#     _initial_guesses = initial_guesses(_equations[0], _vars, _constants)
#     print("Jacobian:\t", _jacobian)
#     print("Equations:\t",_equations)
#     print("Variables:\t",_vars)
#     print("Constants:\t",_constants)
#     print("Initial Guesses:\t",initial_guesses(_equations[0], _vars, _constants))
#     # initial_guess_of_solution = 
#     number_of_iterations = 0
#     _vars_delta = [0 for i in range(len(_vars))]
    
    
    
#     while (number_of_iterations < max_iter):
#         # for i in range(len(_vars)):
#         #     _vars_delta[i] = _equations[i].subs(_initial_guesses) / _jacobian[i][i].subs(_initial_guesses)
#         #     _initial_guesses[_vars[i]] = _initial_guesses[_vars[i]] - _vars_delta[i]
#         # number_of_iterations += 1
#         # print(_vars_delta)
#         # if (all(abs(delta) < esp for delta in _vars_delta)):
#         #     return _initial_guesses
#         # delta = sympy.Matrix(_jacobian).inv() * sympy.Matrix([equation.subs(_initial_guesses) for equation in _equations])
        
#         delta = numpy.linalg(_jacobian, equations.subs(_initial_guesses))
#         _initial_guesses = {var: _initial_guesses[var] - delta[i] for i, var in enumerate(_vars)}
#         number_of_iterations += 1
        
#         if (all(abs(delta) < esp for delta in _vars_delta)):
#             print("Number of iterations:\t",number_of_iterations)
#             return _initial_guesses
    
#     return 0


import sympy as sym
import math
sym.init_printing()
x,y,z = sym.symbols('x,y,z')
c1 = sym.Symbol('c1')
f = sym.Eq(2*x**2+y+z,1)
g = sym.Eq(x+2*y+z, c1)
h = sym.Eq(-2*x+y, -z)
l = [f, g, h]
a = [x, y, z]
print(l,type(l))
print(a,type(a))
print(sym.solve([f,g,h],[x,y,z]))