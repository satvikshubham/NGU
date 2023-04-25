from gekko import GEKKO
m = GEKKO()

Mpa = m.Var()
Msa1 = m.Var()
Msa2 = m.Var()
Msa3 = m.Var()
P1 = m.Var()
P1ppp = m.Var()
P2 = m.Var()
P2p = m.Var()
P3 = m.Var()
P3p = m.Var()
P3pp = m.Var()
P3ppp = m.Var()
P4 = m.Var()
P5 = m.Var()
P5p = m.Var()
P5pp = m.Var()
P5ppp = m.Var()
P6 = m.Var()
P7 = m.Var()
P7p = m.Var()
P7pp = m.Var()
P7ppp = m.Var()
P8 = m.Var()
P9 = m.Var()
P9p = m.Var()

rhoA = 1.1729
kent = 0.5
A1 = 0.0024
rhoT = 0.4689
kbend = 1
kexp = 0.4
A2 = 0.0064
g = 9.81
z2 = 0.03
kcont = 0.3
A3 = 0.0064
z3 = 0.08
C1 = 180
C2 = 2.9101e+03
z3pp = 0.095
z3p = 0.095
A3pp = 0.0018
d4 = 0.08
A4 = 0.0064
z4 = 0.11
A5 = 0.0064
z5 = 0.14
z5pp = 0.1465
z5p = 0.1465
A5pp = 1.3273e-04
z6 = 0.153
z7 = 0.159
n1 = 10
A7 = 0.0064
A6 = 0.0064
z7pp = 0.1655
z7p = 0.1655
A7pp = 1.3273e-04
z8 = 0.172
z9 = 0.2015
n2 = 7
A9 = 0.0064
A8 = 0.0064
kexit = 1
A1ppp = 0.003
A2p = 0.012


m.Equations([-P1/rhoA - (1+kent)*(Mpa/rhoA/A1)**2/2 == 0,
             -P1/rhoA + P2/rhoT + (1+kbend+kexp)*(Mpa/rhoT/A2)**2 /
             2 - (Mpa/rhoA/A1)**2/2 + g*z2 == 0,
             -P2/rhoT + P3/rhoT + (1+kcont)*(Mpa/rhoT/A3)**2/2 - (Mpa/rhoT/A2)**2/2 + g*(
                 z3-z2) + C1*(z3-z2)/rhoT/A2*Mpa + C2*(z3-z2)/rhoT/A2**2*Mpa**2 == 0,
             -P3/rhoT + P3ppp/rhoT + g *
             (z3pp-z3) + C1*(z3pp-z3)/rhoT/A3*Mpa +
             C2*(z3pp-z3)/rhoT/A3**2*Mpa**2 == 0,
             -P3p/rhoA - g*z3p == 0,
             -P3pp/rhoA + P3p/rhoA - (1+kent)*(Msa1/rhoA/A3pp)**2/2 == 0,
             -P3pp/rhoA + P3ppp/rhoT + C1*d4/2/rhoT/A3pp *
             Msa1 + C2*d4/2/rhoT/A3pp**2*Msa1**2 == 0,
             -P3ppp/rhoT + P4/rhoT + (1+kexp)*((Mpa+Msa1)/rhoT/A4)**2/2 - ((Mpa+Msa1)/rhoT/A3)**2 / + g*(
                 z4-z3pp) + C1*(z4-z3pp)/rhoT/A4*(Mpa+Msa1) + C2*(z4-z3pp)/rhoT/A4**2*(Mpa+Msa1)**2 == 0,
             P4/rhoT + P5/rhoT + (1+kexp)*((Mpa+Msa1)/rhoT/A5)**2 /
             2 - ((Mpa+Msa1)/rhoT/A4)**2/2 + g*(z5-z4) == 0,
             -P5/rhoT + P5ppp/rhoT + g*(z5pp-z5) == 0,
             -P2p/rhoA + P5p/rhoA + g*(z5p-z2) == 0,
             -P5pp/rhoA + P5p/rhoA - (0+kent)*(Msa2/rhoA/A5pp)**2/2 == 0,
             -P5pp/rhoA + P5ppp/rhoT +
             (Msa2/rhoT/A5pp)**2/2 - (Msa2/rhoA/A5pp)**2/2 == 0,
             -P5ppp/rhoT + P6/rhoT + g*(z6-z5pp) == 0,
             P6/rhoT + P7/rhoT + g*(z7-z6) + (1)*((Mpa+Msa1+n1*Msa2) /
                                                  rhoT/A7)**2/2 - ((Mpa+Msa1+n1*Msa2)/rhoT/A6)**2/2 == 0,
             -P7/rhoT + P7ppp/rhoT + g*(z7pp-z7) == 0,
             -P5p/rhoA + P7p/rhoA + g*(z7p-z5p) == 0,
             -P7pp/rhoA + P7p/rhoA - (0+kent)*(Msa3/rhoA/A7pp)**2/2 == 0,
             -P7pp/rhoA + P7ppp/rhoT +
             (Msa3/rhoT/A7pp)**2/2 - (Msa3/rhoA/A7pp)**2/2 == 0,
             -P7ppp/rhoT + P8/rhoT + g*(z8-z7pp) == 0,
             -P8/rhoT + P9/rhoT + g*(z9-z8) + (1)*((Mpa+Msa1+n1*Msa2+n2*Msa3) /
                                                   rhoT/A9)**2/2 - ((Mpa+Msa1+n1*Msa2+n2*Msa3)/rhoT/A8)**2/2 == 0,
             -P9/rhoT + P9p/rhoT -
             (1+kexit)*((Mpa+Msa1+n1*Msa2+n2*Msa3)/rhoT/A9)**2/2 == 0,
             -P9p/rhoA - g*z9 == 0,
             -P1ppp/rhoA + P2p/rhoA + (1+kbend+kexp)*((n1*Msa2+n2*Msa3)/rhoA/A2p)**2/2 - (
                 (n1*Msa2+n2*Msa3)/rhoA/A1ppp)**2/2 + g*z2 == 0,
             -P1ppp/rhoA - (1+kent)*((n1*Msa2+n2*Msa3)/rhoA/A1ppp)**2/2 == 0
             ])

m.solve(disp=True)

print("Mpa :\t",Mpa.value)
print("Msa1 :\t",Msa1.value)
print("Msa2 :\t",Msa2.value)
print("Msa3 :\t",Msa3.value)
print("P1 :\t",P1.value)
print("P1ppp :\t",P1ppp.value)
print("P2 :\t",P2.value)
print("P2p :\t",P2p.value)
print("P3 :\t",P3.value)
print("P3p :\t",P3p.value)
print("P3pp :\t",P3pp.value)
print("P3ppp :\t",P3ppp.value)
print("P4 :\t",P4.value)
print("P5 :\t",P5.value)
print("P5p :\t",P5p.value)
print("P5pp :\t",P5pp.value)
print("P5ppp :\t",P5ppp.value)
print("P6 :\t",P6.value)
print("P7 :\t",P7.value)
print("P7p :\t",P7p.value)
print("P7pp :\t",P7pp.value)
print("P7ppp :\t",P7ppp.value)
print("P8 :\t",P8.value)
print("P9 :\t",P9.value)
print("P9p :\t",P9p.value)