import sympy 
sympy.init_printing()
x, y = sympy.symbols('x,y')
f = sympy.Eq(x**2 + x*y, 1)
g = sympy.Eq(y + x , 3)
print(sympy.solve([f, g], [x, y]))
