from gekko import GEKKO
from sympy import *
m = GEKKO()
x = m.Var()
y = m.Var()

gekko_eqs = m.Equations([sin(x*y) - x+y**2 == 1,
             x + y == 0.5
             ])
print(gekko_eqs)

m.solve(disp=False)
print(x.value, y.value)