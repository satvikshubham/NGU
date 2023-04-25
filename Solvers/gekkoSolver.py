# from gekko import GEKKO
# m = GEKKO()
# x,y = [m.Var(1) for i in range(2)]
# m.Equations([x**2 + x*y == 1, y + x == 3])
# m.solve(disp=False)
# print(x.value, y.value)

from gekko import GEKKO
W = 100
s = 10
S = 23


m = GEKKO()
abc, b, c, d, e, f, g, h, i, j = [m.Var(1) for i in range(10)]
m.Equations([5-(W+S*9)*abc+S*9*b-S*20*abc**2+S*20*b**2 == 0,
             W*abc-(W+S*9)*b+S*9*c-S*20*b**2+S*20*c**2 == 0,
             W*b-(W+S*9)*c+S*9*d-S*20*c**2+S*20*d**2 == 0,
             W*c-(W+S*9)*d+S*9*e-S*20*d**2+S*20*e**2 == 0,
             W*d-(W+S*9)*e+S*9*f-S*20*e**2+S*20*f**2 == 0,
             W*e-(W+S*9)*f+S*9*g-S*20*f**2+S*20*g**2 == 0,
             0.039+W*f+(-W+9*S)*g-9*s*h+20*S*g**2-20*s*h**2 == 0,
             W*g-(W+9*s)*h-9*s*i-20*s*h**2-20*s*i**2 == 0,
             W*h-(W+9*s)*i-9*s*j-20*s*i**2-20*s*j**2 == 0,
             W*i-(W+9*s)*j-20*s*j**2 == 0])
m.solve(disp=True)
print(abc.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value, j.value)