import sympy
import numpy
from sympy import solve
from sympy.abc import a,b,c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

def bisection(equations, vals_a, vals_b, vars, tol=1e-6, max_iter=100):
    # if (numpy.sign(equations.subs(vals_a)) == numpy.sign(equations.subs(vals_b))):
    #     print("hi")
    #     raise ValueError("The function must have opposite signs at the endpoints of the interval")
    for i in range(max_iter):
        vals_c = {var: (vals_a[var] + vals_b[var]) / 2 for var in vars}
        if (abs(equations.subs(vals_c)) < tol):
            return vals_c
        if (numpy.sign(equations.subs(vals_a)) == numpy.sign(equations.subs(vals_c))):
            vals_a = vals_c
        else:
            vals_b = vals_c
    raise ValueError("The method failed after {} iterations".format(max_iter))

def initial_guesses(equations, vars, constants):
    val_a = {var: -5 for var in vars}
    val_b = {var: 5 for var in vars}
    stopper = 0
    while (numpy.sign(equations.subs(val_a)) == numpy.sign(equations.subs(val_b))):
        val_a = {var: val_a[var] - 5 for var in vars}
        val_b = {var: val_b[var] + 5 for var in vars}
        stopper += 1
        if (stopper == 100):
            break
    root_interval = bisection(equations, val_a, val_b, vars)
    return root_interval

def compute_jacobian(equations, vars):
    jacobian = []
    for equation in equations:
        row = []
        for var in vars:
            row.append(sympy.diff(equation, var))
        jacobian.append(row)
    return jacobian
    

def set_inputs(equations):
    n = len(equations)
    var_names = []
    for i in range (n):
        var_names.append(chr(ord('a') + i))
    vars = sympy.symbols(var_names)
    equations = [sympy.sympify(equation) for equation in equations]
    # extract constant term from the equations
    constants = [equation.subs({var: 0 for var in vars}) for equation in equations]
    # values = {var: random.randint(0, 10) for var in vars}
    # result = [equation.subs(values) for equation in equations]
    return vars, equations, constants

def Netwon_system(equations, esp = 0.001, max_iter = 100):
    _vars, _equations, _constants = set_inputs(equations)
    _jacobian = numpy.array(compute_jacobian(_equations, _vars))
    _initial_guesses = initial_guesses(_equations[0], _vars, _constants)
    _equations = numpy.array(_equations)
    print("Initial guesses\t",_initial_guesses)
    print("Jacobian\t",_jacobian)
    print("Equations\t",_equations)
    iteration_counter = 0
    F_value = numpy.array([_equation.subs(_initial_guesses) for _equation in _equations])
    print("F_value\t",F_value)
    F_value = F_value.astype(numpy.float64)
    F_norm  = numpy.linalg.norm(F_value, ord=2)
    while (abs(F_norm) > esp and iteration_counter < max_iter):
        delta = solve(_jacobian-F_value, _vars)
        initial_guesses = initial_guesses + delta
        F_value = _equations.subs(_initial_guesses)
        F_norm = numpy.linalg.norm(F_value, ord=2)
        iteration_counter += 1
        
    # while (abs(F_norm) > esp and iteration_counter < max_iter):
    #     delta = numpy.linalg.solve(_jacobian, -F_value)
    #     _initial_guesses = _initial_guesses + delta
    #     F_value = _equations.subs(_initial_guesses)
    #     F_norm = numpy.linalg.norm(F_value, ord=2)
    #     iteration_counter += 1
    
    if (abs(F_norm) > esp):
        iteration_counter = -1
    return _initial_guesses, iteration_counter

def solve(equations, esp = 0.0001, max_iter = 100):
    _vars, _equations, _constants = set_inputs(equations)
    _jacobian = compute_jacobian(_equations, _vars)
    _initial_guesses = initial_guesses(_equations[0], _vars, _constants)
    print("Jacobian:\t", _jacobian)
    print("Equations:\t",_equations)
    print("Variables:\t",_vars)
    print("Constants:\t",_constants)
    print("Initial Guesses:\t",initial_guesses(_equations[0], _vars, _constants))
    # initial_guess_of_solution = 
    number_of_iterations = 0
    _vars_delta = [0 for i in range(len(_vars))]
    
    
    
    while (number_of_iterations < max_iter):
        # for i in range(len(_vars)):
        #     _vars_delta[i] = _equations[i].subs(_initial_guesses) / _jacobian[i][i].subs(_initial_guesses)
        #     _initial_guesses[_vars[i]] = _initial_guesses[_vars[i]] - _vars_delta[i]
        # number_of_iterations += 1
        # print(_vars_delta)
        # if (all(abs(delta) < esp for delta in _vars_delta)):
        #     return _initial_guesses
        # delta = sympy.Matrix(_jacobian).inv() * sympy.Matrix([equation.subs(_initial_guesses) for equation in _equations])
        
        delta = numpy.linalg(_jacobian, equations.subs(_initial_guesses))
        _initial_guesses = {var: _initial_guesses[var] - delta[i] for i, var in enumerate(_vars)}
        number_of_iterations += 1
        
        if (all(abs(delta) < esp for delta in _vars_delta)):
            print("Number of iterations:\t",number_of_iterations)
            return _initial_guesses
    
    return 0


equations = ["a*b + c - 10", "a + b - 5", "cos(a*b) - 2"]
n = len(equations)
print(Netwon_system(equations))
