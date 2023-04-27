import sympy
sympy.init_printing()
100 = 100
10 = 10
23 = 23

a, b, c, d, e, f, g, h, i, j = sympy.symbols('a,b,c,d,e,f,g,h,i,j')
# f = sympy.Eq(x**2 + x*y, 1)
# g = sympy.Eq(y + x , 3)
# print(sympy.solve([f, g], [x, y]))
aa = sympy.Eq(5-(100+23*9)*a+23*9*b-23*20*a**2+23*20*b**2, 0)
ab = sympy.Eq(100*a-(100+23*9)*b+23*9*c-23*20*b**2+23*20*c**2, 0)
ac = sympy.Eq(100*b-(100+23*9)*c+23*9*d-23*20*c**2+23*20*d**2, 0)
ad = sympy.Eq(100*c-(100+23*9)*d+23*9*e-23*20*d**2+23*20*e**2, 0)
ae = sympy.Eq(100*d-(100+23*9)*e+23*9*f-23*20*e**2+23*20*f**2, 0)
af = sympy.Eq(100*e-(100+23*9)*f+23*9*g-23*20*f**2+23*20*g**2, 0)
ag = sympy.Eq(0.039+100*f+(-100+9*23)*g-9*10*h+20*23*g**2-20*10*h**2, 0)
ah = sympy.Eq(100*g-(100+9*10)*h-9*10*i-20*10*h**2-20*10*i**2, 0)
ai = sympy.Eq(100*h-(100+9*10)*i-9*10*j-20*10*i**2-20*10*j**2, 0)
aj = sympy.Eq(100*i-(100+9*10)*j-20*10*j**2, 0)

print(sympy.solve([aa, ab, ac, ad, ae, af, ag, ah, ai, aj], [a, b, c, d, e, f, g, h, i, j]))