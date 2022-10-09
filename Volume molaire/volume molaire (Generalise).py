import numpy as np
try:
    a = input("Entrez la valeur de a: ")
    b = input("Entrez la valeur de b: ")
    T = input("Entrez la valeur de T en K: ")
    P = input("Entrez la valeur de P en bar: ")
    R = 0.082
except:
    print("la valeur entree n'est pas un nombre")
B = -(P*b+R*T)
C = -a*b
coeff = [P, B, a,C]
sol = np.roots(coeff)
print("valeur de volume molaire =", sol[0].real)