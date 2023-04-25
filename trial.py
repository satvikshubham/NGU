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
C1 = 328.1896
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
             -P3ppp/rhoT + P4/rhoT + (1+kexp)*((Mpa+Msa1)/rhoT/A4)**2/2 - ((Mpa+Msa1)/rhoT/A3)**2/2 + g*(
                 z4-z3pp) + C1*(z4-z3pp)/rhoT/A4*(Mpa+Msa1) + C2*(z4-z3pp)/rhoT/A4**2*(Mpa+Msa1)**2 == 0,
             -P4/rhoT + P5/rhoT + (1+kexp)*((Mpa+Msa1)/rhoT/A5)**2 /
             2 - ((Mpa+Msa1)/rhoT/A4)**2/2 + g*(z5-z4) == 0,
             -P5/rhoT + P5ppp/rhoT + g*(z5pp-z5) == 0,
             -P2p/rhoA + P5p/rhoA + g*(z5p-z2) == 0,
             -P5pp/rhoA + P5p/rhoA - (0+kent)*(Msa2/rhoA/A5pp)**2/2 == 0,
             -P5pp/rhoA + P5ppp/rhoT +
             (Msa2/rhoT/A5pp)**2/2 - (Msa2/rhoA/A5pp)**2/2 == 0,
             -P5ppp/rhoT + P6/rhoT + g*(z6-z5pp) == 0,
             -P6/rhoT + P7/rhoT + g *
             (z7-z6) + (1)*((Mpa+Msa1+n1*Msa2)/rhoT/A7)**2 /
             2 - ((Mpa+Msa1+n1*Msa2)/rhoT/A6)**2/2 == 0,
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


Mpa_actual = 16.15
Msa1_actual = 6.54
Msa2_actual = 95.76
Msa3_actual = 67.03
P1_actual = -0.011
P1ppp_actual = -0.72
P2_actual = -0.146
P2p_actual = -0.657
P3_actual = -1.54
P3p_actual = -1.093
P3pp_actual = -1.096
P3ppp_actual = -1.958
P4_actual = -2.58
P5_actual = -2.72
P5p_actual = -1.997
P5pp_actual = -2.421
P5ppp_actual = -2.750
P6_actual = -2.78
P7_actual = -2.808
P7p_actual = -2.216
P7pp_actual = -2.64
P7ppp_actual = -2.838
P8_actual = -2.867
P9_actual = -3.003
P9p_actual = -2.319


print("Mpa :\t", Mpa.value, " Actual value:\t", Mpa_actual)
print("Msa1 :\t", Msa1.value, " Actual value:\t", Msa1_actual)
print("Msa2 :\t", Msa2.value, " Actual value:\t", Msa2_actual)
print("Msa3 :\t", Msa3.value, " Actual value:\t", Msa3_actual)
print("P1 :\t", P1.value, " Actual value:\t", P1_actual)
print("P1ppp :\t", P1ppp.value, " Actual value:\t", P1ppp_actual)
print("P2 :\t", P2.value, " Actual value:\t", P2_actual)
print("P2p :\t", P2p.value, " Actual value:\t", P2p_actual)
print("P3 :\t", P3.value, " Actual value:\t", P3_actual)
print("P3p :\t", P3p.value, " Actual value:\t", P3p_actual)
print("P3pp :\t", P3pp.value, " Actual value:\t", P3pp_actual)
print("P3ppp :\t", P3ppp.value, " Actual value:\t", P3ppp_actual)
print("P4 :\t", P4.value, " Actual value:\t", P4_actual)
print("P5 :\t", P5.value, " Actual value:\t", P5_actual)
print("P5p :\t", P5p.value, " Actual value:\t", P5p_actual)
print("P5pp :\t", P5pp.value, " Actual value:\t", P5pp_actual)
print("P5ppp :\t", P5ppp.value, " Actual value:\t", P5ppp_actual)
print("P6 :\t", P6.value, " Actual value:\t", P6_actual)
print("P7 :\t", P7.value, " Actual value:\t", P7_actual)
print("P7p :\t", P7p.value, " Actual value:\t", P7p_actual)
print("P7pp :\t", P7pp.value, " Actual value:\t", P7pp_actual)
print("P7ppp :\t", P7ppp.value, " Actual value:\t", P7ppp_actual)
print("P8 :\t", P8.value, " Actual value:\t", P8_actual)
print("P9 :\t", P9.value, " Actual value:\t", P9_actual)
print("P9p :\t", P9p.value, " Actual value:\t", P9p_actual)

