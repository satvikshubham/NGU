# from gekko import GEKKO
# m = GEKKO()
# x,y = [m.Var(1) for i in range(2)]
# m.Equations([x**2 + x*y == 1, y + x == 3])
# m.solve(disp=False)
# print(x.value, y.value)

from gekko import GEKKO

m = GEKKO()
abc, b, c, d, k, f, g, h, i, j = [m.Var(1) for i in range(10)]
m.Equations([5-(100+23*9)*abc+23*9*b-23*20*abc**2+23*20*b**2 == 0,
             100*abc-(100+23*9)*b+23*9*c-23*20*b**2+23*20*c**2 == 0,
             100*b-(100+23*9)*c+23*9*d-23*20*c**2+23*20*d**2 == 0,
             100*c-(100+23*9)*d+23*9*k-23*20*d**2+23*20*k**2 == 0,
             100*d-(100+23*9)*k+23*9*f-23*20*k**2+23*20*f**2 == 0,
             100*k-(100+23*9)*f+23*9*g-23*20*f**2+23*20*g**2 == 0,
             0.039+100*f+(-100+9*23)*g-9*10*h+20*23*g**2-20*10*h**2 == 0,
             100*g-(100+9*10)*h-9*10*i-20*10*h**2-20*10*i**2 == 0,
             100*h-(100+9*10)*i-9*10*j-20*10*i**2-20*10*j**2 == 0,
             100*i-(100+9*10)*j-20*10*j**2 == 0])
m.solve(disp=False)
print(abc.value, b.value, c.value, d.value, k.value, f.value, g.value, h.value, i.value, j.value)