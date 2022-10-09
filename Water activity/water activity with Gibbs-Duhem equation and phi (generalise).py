import numpy as np
try:
    Tf = input("Entrez la valeur de Tf en K: ")
    R = 8.314
    DH = 6009.5
    DCp = 37.87
    nu = 2
    MH2O = 18.01528
    x = input("Entrez la valeur de fraction molaire du solute: ")

except:
    print("la valeur entree n'est pas un nombre")
A = -DH/R
B = 1/Tf
C = 1/273.15
D = DCp/R
E = Tf-273.15
F = Tf/273.15
G = E/Tf
H = np.log(F)
lnaw = (A*(B-C)-D*(G-H))
aw = np.exp(lnaw)
M = ((x*1000)/((1-x)*MH2O))
print("valeur de l'activite de l'eau =", aw)
Phi = ((-1000*lnaw)/(nu*M*MH2O))
print("valeur de Phi =", Phi)