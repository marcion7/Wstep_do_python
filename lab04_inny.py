# 1

# zdanie = input("Podaj zdanie: ")
# print(f"Zdanie zawiera {zdanie.count(' ')} spacji.")

# 2
# import sys
#
# print("Podaj liczby:")
# liczba1 = sys.stdin.readline()
# liczba2 = sys.stdin.readline()
# suma = int(liczba1) + int(liczba2)
# sys.stdout.write(str(suma))

# 3

# a = input('Podaj a: ')
# a = int(a)
# b = input('Podaj b: ')
# b = int(b)
# c = input('Podaj c: ')
# c = int(c)
# if(a > 0 and a <= 10 and a > b):
#     print('A zawiera się w przedziale (0,10] i a > b')
# elif(a > 0 and a <= 10 and b > c):
#     print('A zawiera się w przedziale (0,10] i b > c')
# else:
#     print('A NIE zawiera się w przedziale (0,10] i/lub inne warunki nie zostały spełnione')

# 4

# i = 0
# while i <= 50:
#     if i % 5 == 0:
#         print(i)
#     i += 1

# 5

# while True:
#     kwadraty = input("Wpisz liczby odzielone spacjami: ")
#     if kwadraty.__contains__('quit'):
#         break
#     listakwadratow = kwadraty.split(' ')
#     for i in listakwadratow:
#         print(int(i) * int(i))

# 6

# listaliczb = []
# while True:
#     liczby = input("Podaj liczbę: ")
#     if liczby != 'stop':
#         liczby = int(liczby)
#         listaliczb.append(liczby)
#         print(listaliczb)
#     else:
#         break

# 7

# liczbawielocyfrowa = input("Podaj liczbę wielocyfrową: ")
# i = 0
# suma = 0
# while i < len(liczbawielocyfrowa):
#     suma += int(liczbawielocyfrowa[i])
#     i += 1
# print(suma)

# 8

def wieza(a):
    i = 1
    if (a > 0 and a <= 10):
        for i in range(a+1):
            print('A' * i)
            i += 1

wieza(8)

# 9

for a in range(1,11):
    for b in range(1,11):
        print(f'{a} * {b} = {a*b}')

# 10

def diament(a):
    if (a > 2 and a < 10):
        i = 1
        j = 1
        while j <= a:
            print('o' * j)
            j += 2
            j -= 2
            print('o' * j)
diament(3)