# 1
import csv
from datetime import date

with open('zamowienia.csv', newline='', encoding='utf-8', errors='replace') as csvfile:
    with open('zamowienia_polska.csv', 'w', newline='') as csvfile_polska:
        with open('zamowienia_niemcy.csv', 'w', newline='') as csvfile_niemcy:
            kolumny = ['Kraj','Sprzedawca','Data zamowienia','idZamowienia','Utarg']
            writer_pl = csv.DictWriter(csvfile_polska, fieldnames=kolumny)
            writer_ni = csv.DictWriter(csvfile_niemcy, fieldnames=kolumny)
            writer_pl.writeheader()
            writer_ni.writeheader()
            reader = csv.DictReader(csvfile, delimiter=';')
            for wiersz in reader:
                wiersz["Utarg"] = wiersz["Utarg"].replace(',', '.')
                wiersz["Utarg"] = wiersz["Utarg"].replace(' ', '')
                wiersz["Utarg"] = wiersz["Utarg"].split('z')[0]
                data = wiersz["Data zamowienia"].split('.')
                wiersz["Data zamowienia"] = date(int(data[2]), int(data[1]), int(data[0])) if len(data) > 1 else data[0]
                if wiersz["Kraj"] == 'Polska':
                    writer_pl.writerow(wiersz)
                elif wiersz["Kraj"] == 'Niemcy':
                    writer_ni.writerow(wiersz)


# 2
def scal(lista, nowyplik):
    uchwyt = open(nowyplik, 'w', encoding='utf-8')
    for nazwa in lista:
        with open(nazwa, 'r', encoding='utf-8') as file_reader:
            uchwyt.write(file_reader.read())
    uchwyt.close()

# scal(['plik1.txt', 'plik2.txt', 'plik3.txt'], 'nowyplik.txt')


# 3
def n_naj(lista, ilosc, kolejnosc):
    for i in lista:
        if type(i) == int or type(i) == float:
            continue
        else:
            return 'lista nie zawiera tylko liczb'
    if kolejnosc == 'ros':
        lista.sort()
    elif kolejnosc == 'mal':
        lista.sort(reverse=True)
    else:
        return 'wartość 3 parametru może być tylko "ros" lub "mal"'

    elementy = ''
    for i in range(ilosc):
        if ilosc > len(lista):
            return 'lista nie zawiera tylu elementów'
        else:
            elementy += str(lista[i]) + ' '
    return elementy

print(n_naj([1,1.25,1.5], 2, 'mal'))

# 4
mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
def slownik_wartosci(lista):
    slownik = {}
    for i in lista:
        if str(type(i)).split("'")[1] not in slownik.keys():
            slownik[str(type(i)).split("'")[1]] = [i]
        else:
            slownik[str(type(i)).split("'")[1]] += [i]
    return slownik

print(slownik_wartosci(mieszana))

# 5
from unidecode import unidecode

def rozdziel_nazwiska(lista):
    AM = open('A-M_nazwiska.txt', 'w', encoding='utf-8')
    NZ = open('N-Ż_nazwiska.txt', 'w', encoding='utf-8')
    for i in lista:
        if ord(unidecode(i)[0]) >= 65 and ord(unidecode(i)[0]) <= 77:
            AM.write(i + ' ')
        elif ord(unidecode(i)[0]) >= 78 and ord(unidecode(i)[0]) <= 90:
            NZ.write(i + ' ')
    AM.close()
    NZ.close()

rozdziel_nazwiska(['ALa','Żaba','Baba','Saba','Nowak','Kowalski'])

# 6
def odwroc_wyrazy(zdanie):
    rozdzieone = zdanie.split()
    nowezdanie = ''
    for i in rozdzieone:
        for j in range(len(i)-1, -1, -1):
            nowezdanie += i[j]
        nowezdanie += ' '
    return nowezdanie

print(odwroc_wyrazy('Ala ma kota'))

# 7
import random

talia = ['2 pik','3 pik','4 pik','5 pik','6 pik','7 pik','8 pik','9 pik','10 pik','walet pik','dama pik','król pik','as pik',
         '2 kier','3 kier','4 kier','5 kier','6 kier','7 kier','8 kier','9 kier','10 kier','walet kier','dama kier','król kier','as kier',
         '2 karo','3 karo','4 karo','5 karo','6 karo','7 karo','8 karo','9 karo','10 karo','walet karo','dama karo','król karo','as karo',
         '2 trefl','3 trefl','4 trefl','5 trefl','6 trefl','7 trefl','8 trefl','9 trefl','10 trefl','walet trefl','dama trefl','król trefl','as trefl']

def rozdaj_5kart(gracze):
    if len(gracze) != 4:
        return 'Podaj listę 4 graczy'
    slownik = {}
    wylosowane = []
    nr_gracza = 0
    while len(wylosowane) <= 20:
        karta = random.randint(0, 51)
        if karta not in wylosowane:
            wylosowane.append(karta)
            if gracze[nr_gracza] not in slownik.keys():
                slownik[gracze[nr_gracza]] = [talia[karta]]
            else:
                slownik[gracze[nr_gracza]] += [talia[karta]]
            if nr_gracza == 3:
                nr_gracza = 0
            else:
                nr_gracza += 1
        else:
            continue
    return slownik

print(rozdaj_5kart(['Marek', 'Bartek', 'Janek', 'Marcin']))

# 8
def dodaj_email(plik, domena):
    with open(plik, 'r', encoding='utf-8') as file_reader:
        emaile = open('emaile.txt', 'w', encoding='utf-8')
        for linia in file_reader:
            linia = linia.replace('\n', '')
            email = linia.lower()
            email = unidecode(email)
            email = email.replace(' ', '.')
            email += '@' + domena + '\n'
            emaile.write(linia + ', ' + email)

dodaj_email('imiona_nazwiska.txt', 'student.uwm.edu.pl')

# 9
hasla = []
with open('kolo_fortuny.txt', 'r', encoding='utf-8') as file_reader:
    for linia in file_reader:
        linia = linia.replace('\n', '')
        hasla.append(linia)

haslo = hasla[random.randint(0, len(hasla)-1)]
ukryte = ''
for i in haslo:
    if i != ' ':
        i = '_'
    ukryte += i

list_haslo = list(haslo)
list_ukryte = list(ukryte)
zmod_haslo = haslo

while '_' in list_ukryte:
    print(ukryte)
    strzal = input('Podaj literę lub odgadnij hasło: ')
    if len(strzal) == 1:
        if strzal.lower() in list_haslo or strzal.upper() in list_haslo:
            while zmod_haslo.find(strzal.lower()) != -1 or zmod_haslo.find(strzal.upper()) != -1:
                if zmod_haslo.find(strzal.lower()) != -1:
                    list_ukryte[list_haslo.index(strzal)] = list_haslo[list_haslo.index(strzal)]
                    list_haslo[list_haslo.index(strzal)] = '_'
                else:
                    list_ukryte[list_haslo.index(strzal.upper())] = list_haslo[list_haslo.index(strzal.upper())]
                    list_haslo[list_haslo.index(strzal.upper())] = '_'
                ukryte = "".join(list_ukryte)
                zmod_haslo = "".join(list_haslo)
        else:
            print('Haslo nie zawiera litery: ' + strzal)
    else:
        if strzal == haslo:
            list_ukryte = haslo
        else:
            print('Haslo niepoprawne!')
    if '_' not in list_ukryte:
        print("BRAWO!!! Poprawne hasło to: " + haslo)



