import numpy as np
try:
    T= input ("Entrez la valeur de Tf en K: ")
    x = input("Entrez la valeur de fraction molaire de solute: ")
    M = 18.01528
    nu = input("Entrez la valeur de nu: ")
    cst = 1.858
#(nu is the number of molecules formed per molecule of solute)
except:
    print("la valeur entree n'est pas un nombre")
DT = 273.15-T
m = ((x*1000)/((1-x)*M))
Phi = DT/(nu*m*cst)
print("valeur de Phi =", Phi)