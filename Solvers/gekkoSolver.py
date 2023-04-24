from gekko import GEKKO
m = GEKKO()
x,y = [m.Var(1) for i in range(2)]
m.Equations([x**2 + x*y == 1, y + x == 3])
m.solve(disp=True)
print(x.value, y.value)