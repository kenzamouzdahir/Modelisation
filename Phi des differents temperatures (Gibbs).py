import math
R = 8.314
A = 6009.5
B = 37.87
nu = 2
MH2O = 18.01528
Tf_list = []

Tf_list.append(['Tf=272.35', 272.35, 0.0077])
Tf_list.append(['Tf=271.25', 271.25, 0.0187])
Tf_list.append(['Tf=269.95', 269.95, 0.034])
Tf_list.append(['Tf=266.35', 266.35, 0.0739])
Tf_list.append(['Tf=263.95', 263.95, 0.0958])
Tf_list.append(['Tf=261.05', 261.05, 0.137])
Tf_list.append(['Tf=259.35', 259.35, 0.1428])
Tf_list.append(['Tf=257.65', 257.65, 0.1663])
Tf_list.append(['Tf=254.75', 354.75, 0.1958])
Tf_list.append(['Tf=252.75', 252.75, 0.2321])
Tf_list.append(['Tf=249.35', 249.35, 0.2715])
Tf_list.append(['Tf=246.15', 246.15, 0.2937])

for Tf in Tf_list:
    lnaw = ((-A/R)*((1/Tf[1])-(1/273.15)))-((B/R)*(((Tf[1]-273.15)/Tf[1])-(math.log(Tf[1]/273.15))))
    aw = math.exp(lnaw)
    M = ((Tf[2]*1000)/((1-Tf[2])*MH2O))
    print("valeur de l'activite de l'eau de", Tf[0], "est =", aw)
    Phi = ((-1000*lnaw)/(nu*M*MH2O))
    print("valeur de Phi de ", Tf[0], " est =", Phi)