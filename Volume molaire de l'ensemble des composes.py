import numpy as np

R = 0.082
T = 773.15
P = 197.38
gas_list = []
gas_list.append(['He', 0.03412, 0.0237])
gas_list.append(['Ne', 0.2107, 0.01709])
gas_list.append(['O2', 1.36, 0.03183])
gas_list.append(['N2', 1.39, 0.03913])
gas_list.append(['CH4', 2.253, 0.04278])
gas_list.append(['HCl', 3.667, 0.04081])
gas_list.append(['CO2', 3.592, 0.04267])
gas_list.append(['NH3', 4.17, 0.03707])
gas_list.append(['H2O', 5.464, 0.03049])
gas_list.append(['Cl2', 6.493, 0.05622])
gas_list.append(['Hg', 8.093, 0.01696])

for gas in gas_list:
    B = -(P * gas[2] + R * T)
    C = -gas[1] * gas[2]
    coeff = [P, B, gas[1], C]
    sol = np.roots(coeff)
    print("valeur de volume molaire de ", gas[0], " est =", sol[0].real)