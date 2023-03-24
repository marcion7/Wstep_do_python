# 1

liczba = int(input('Podaj liczbe całkowitą: '))
print(f'Liczba {liczba} to : binarnie: {bin(liczba)}, ósemkowo: {oct(liczba)},szesnastowo: {hex(liczba)}')

# 2

wartosc = input('Podaj wartość: ')
if type(int(wartosc)) == int:
    print('wartość jest rzutowalna na int')
if type(float(wartosc)) == float:
    print('wartość jest rzutowalna na float')

# 3
import sys

print("Podaj liczbę: ")
wynik = "Podaną liczbę można zapisać jako: "
liczba = sys.stdin.readline()
mnoznik = 10 ** len(liczba)
for i in range(len(liczba) - 1):
    mnoznik /= 10
    if liczba[i] == '0':
        continue
    licz = f"{mnoznik/10} * {liczba[i]}"
    wynik += licz
    if mnoznik != 10:
        wynik +=" + "
sys.stdout.write(wynik)

# 4

import this

zdanie = input('Podaj zdanie: ')
zakodowane = ""
for i in zdanie:
    if i not in this.d.keys():
        zakodowane += i
    else:
        zakodowane += this.d.get(i)
print(zakodowane)

# 5

zdanie = input('Podaj zdanie: ')
wyrazy = zdanie.split(' ')
slownik = {}
for i in wyrazy:
    if len(i) in slownik.keys():
        slownik[len(i)] += ' ' + i
    else:
        slownik[len(i)] = i
posortowane = sorted(slownik.items())
zdanie_sort = ''
for i in posortowane:
    zdanie_sort += i[1]
    if i != len(posortowane):
        zdanie_sort += ' '
print(zdanie_sort)

# 6
import random

tabela = [
['Koleżanki i koledzy', 'realizacja nakreślonych zadań programowych', 'zmusza nas do przeanalizowania istniejących warunków', 'administracyjno-finansowych.'],
['Z drugiej strony', 'zakres i miejsce szkolenia kadr',	'spełnia istotną rolę w kształtowaniu', 'dalszych kierunków rozwoju.'],
['Podobnie', 'stały wzrost ilości i zakres naszej aktywności', 'wymaga sprecyzowania i określenia', 'systemu powszechnego uczestnictwa.'],
['Nie zapominajmy jednak, że', 'aktualna struktura organizacji', 'pomaga w przygotowaniu i realizacji', 'postaw uczestników wobec zadań stawianych przez organizację.'],
['W ten oto sposób', 'nowy model działalności organizacyjnej', 'zabezpiecza udział szerokiej grupie w kształtowaniu', 'nowych propozycji.'],
['Praktyka dnia codziennego dowodzi, że', 'dalszy rozwój różnych form działalności', 'spełnia ważne zadania w wypracowaniu', 'kierunków postępowego wychowania.'],
['Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ', 'stałe zabezpieczenie informacyjno programowe naszej działalności',	'umożliwia w większym stopniu tworzenie', 'systemu szkolenia kadry odpowiadającego potrzebom.'],
['Różnorakie i bogate doświadczenia', 'wzmacnianie i rozwijanie struktur',	'powoduje docenianie wagi',	'odpowiednich warunnków aktywizacji.'],
['Troska organizacji, a szczególnie', 'konsultacja z szerokim aktywem', 'przedstawia intersującą próbę sprawdzenia', 'modelu rozwoju.'],
['Wyższe założenia ideowe, a także', 'rozpoczęcie powszechnej akcji kształtowania postaw', 'pociąga za sobą proces wdrażania i unowocześniania', 'form oddziaływania.']
]

ilosc = input('Podaj ilość zdań: ')
ilosc = int(ilosc)
for i in range(ilosc):
    zdanie = ''
    for j in range(len(tabela[0])):
        zdanie += tabela[random.randint(0,9)][j]
        if i != len(tabela[0]):
            zdanie += ' '
    print(zdanie)