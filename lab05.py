# 1

A = {1/x for x in range(1,10)}
B = {2 ** x for x in range(1,10)}
C = {x for x in B if x % 4 == 0}

print(A)
print(B)
print(C)

# 2

import random

macierz = []
for i in range(4):
    wiersz = []
    for j in range(4):
        wiersz.append(random.randint(0,100))
    macierz.append(wiersz)

print(macierz)

przekatna = [macierz[i][i] for i in range(len(macierz[0]))]

print(przekatna)

# 3

zdanie = 'Ala ma kota.'
przeliteruj = (l for l in zdanie)
wyraz = ''
lista_znakow = []
i = next(przeliteruj, None)
while i != None:
    if i != ' ' and i != '.':
        wyraz += i
        lista_znakow.append(ord(i))
    else:
        krotka = (wyraz, lista_znakow)
        wyraz = ''
        lista_znakow = []
        print(krotka)
    i = next(przeliteruj, None)
# 4

import math

def row_kwadratowe(a: int, b: int, c: int) -> float:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

# 5

def rzuc(n: int) -> list:
    n = int(input('Podaj liczbę rzutów: '))
    lista = []
    oczka = 0
    for i in range(1,n+1):
        oczka += random.randint(1,6)
        tuple = (f'oczka: {oczka}', f'rzutów: {i}')
        lista.append(tuple)
    return lista

print(rzuc(5))

# 6

def ciag(* napisy):
    if len(napisy) == 0:
        return 'nie podano żadnego napisu'
    else:
        return sorted(napisy)

print(ciag('cab','cb','aba'))

# 7

def zlicz(**druzyny):
    suma = 0
    for pkty in druzyny:
        suma += int(druzyny[pkty])
    print(f'Wszystkie pkty: {suma}')

zlicz(a=1,b=2)