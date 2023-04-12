import math
from pyneqsys.symbolic import SymbolicSys


def powell(x, params, backend=math):
    A, exp = params[0], backend.exp
    return A*x[0]*x[1] - 1, exp(-x[0]) + exp(-x[1]) - (1 + A**-1)

powell_sys = SymbolicSys.from_callback(powell, 2, 1, names='x0 x1'.split())
x, info = powell_sys.solve([1, 1], [1000.0])

print(', '.join(['%.6e' % _ for _ in sorted(x)]))