from pyneqsys.symbolic import SymbolicSys
from sympy.parsing.sympy_parser import parse_expr
from sympy import *

neqsys = SymbolicSys.from_callback(
    lambda x: [(x[0] - x[1])**1/2 + x[0] - 1,
               (sin(x[0]) - x[1])**2 + x[0] - 1,
               ], 2)



x, info = neqsys.solve([1, 2])


assert info['success']
print(x)