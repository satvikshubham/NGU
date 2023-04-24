import sympy
sympy.init_printing()
W = 100
s = 10
S = 23

a, b, c, d, e, f, g, h, i, j = sympy.symbols('a,b,c,d,e,f,g,h,i,j')
# f = sympy.Eq(x**2 + x*y, 1)
# g = sympy.Eq(y + x , 3)
# print(sympy.solve([f, g], [x, y]))
aa = sympy.Eq(5-(W+S*9)*a+S*9*b-S*20*a**2+S*20*b**2, 0)
ab = sympy.Eq(W*a-(W+S*9)*b+S*9*c-S*20*b**2+S*20*c**2, 0)
ac = sympy.Eq(W*b-(W+S*9)*c+S*9*d-S*20*c**2+S*20*d**2, 0)
ad = sympy.Eq(W*c-(W+S*9)*d+S*9*e-S*20*d**2+S*20*e**2, 0)
ae = sympy.Eq(W*d-(W+S*9)*e+S*9*f-S*20*e**2+S*20*f**2, 0)
af = sympy.Eq(W*e-(W+S*9)*f+S*9*g-S*20*f**2+S*20*g**2, 0)
ag = sympy.Eq(0.039+W*f+(-W+9*S)*g-9*s*h+20*S*g**2-20*s*h**2, 0)
ah = sympy.Eq(W*g-(W+9*s)*h-9*s*i-20*s*h**2-20*s*i**2, 0)
ai = sympy.Eq(W*h-(W+9*s)*i-9*s*j-20*s*i**2-20*s*j**2, 0)
aj = sympy.Eq(W*i-(W+9*s)*j-20*s*j**2, 0)

print(sympy.solve([aa, ab, ac, ad, ae, af, ag, ah, ai, aj], [a, b, c, d, e, f, g, h, i, j]))