print("Program obliczający układ równań z 3 niewiadomymi\n")
tab = []
row = [0, 0, 0]
eq = []
for i in range(3):
    tab.append(row[:])
for i in range(3):
    for j in range(3):
        tab[i][j] = int(input("Podaj współczynnik przy niewiadomej: "))
    eq.append(int(input("Podaj wynik równania: ")))


def podmien(tin, tfrom, col):
    tab1 = []
    for i in range(3):
        tab1.append([0, 0, 0])
    for i in range(3):
        for j in range(3):
            tab1[i][j] = tin[i][j]
    for i in range(3):
        tab1[i][col] = int(tfrom[i])
    return tab1


def wyznacznik(t):
    return t[0][0]*t[1][1]*t[2][2] + t[1][0]*t[2][1]*t[0][2] + t[2][0]*t[0][1]*t[1][2] - \
           t[2][0]*t[1][1]*t[0][2] - t[1][0]*t[0][1]*t[2][2] - t[0][0]*t[2][1]*t[1][2]


W = wyznacznik(tab)
Wx = wyznacznik(podmien(tab, eq, 0))
Wy = wyznacznik(podmien(tab, eq, 1))
Wz = wyznacznik(podmien(tab, eq, 2))
#print(W, Wx, Wy, Wz)

if W != 0:
    print("\nNiewiadomymi są: \nx = ", Wx/W)
    print("y = ", Wy/W)
    print("z = ", Wz/W)
elif W == 0 and Wx == 0 and Wy == 0 and Wz == 0:
    print("\nUkład nieoznaczony.")
else: print("\nUkłąd sprzeczny.")
#print(tab)
input()

#KACZOROWSKI BARTOSZ