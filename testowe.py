# Sprawdzanie wyrazeniem reguralnym czy poprawne imie i nazwisko
import math
import random
import re


def czy_poprawny(str):
    wzor = re.compile('^[A-Z][a-z]+ [A-Z][a-z]+')
    if re.fullmatch(wzor, str) is None:
        return False
    else:
        return True


# print(czy_poprawny('Jan Kowalski'))

# Zadanie: Rejestracja użytkownika Napisz program, który poprosi użytkownika o podanie swojego imienia, nazwiska, adresu e-mail i hasła.
# Następnie zapisz te dane do pliku tekstowego jako nowy rekord w formacie CSV.

import csv


# with open('dane_uzytkownika.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([input("Podaj imie: "), input("Podaj nazwisko: "), input("Podaj email: "), input("Podaj haslo: ")])

# Zadanie: Gra w zgadywanie liczby
# Napisz prostą grę, w której komputer losuje liczbę z zakresu od 1 do 100, a użytkownik ma za zadanie zgadnąć tę liczbę w jak
# najmniejszej liczbie prób. Po każdej próbie program informuje użytkownika, czy podana liczba jest za duża, za mała czy równa wylosowanej liczbie.

def zgadnij_liczbe():
    los_liczbe = random.randint(1, 100)
    liczba = int(input("Podaj liczbę: "))
    ilosc_prob = 1
    while liczba != los_liczbe:
        if los_liczbe > liczba:
            print("Szukana liczba jest większa")
        else:
            print("Szukana liczba jest mniejsza")
        ilosc_prob += 1
        liczba = int(input("Podaj liczbę: "))
    print(f"Brawo! Zgadłeś, że poprawna liczba to: {los_liczbe} za {ilosc_prob} razem.")


# zgadnij_liczbe()

# Zadanie: Kalkulator pola powierzchni
# Napisz program, który pozwoli użytkownikowi wybrać jedną z trzech figur geometrycznych (kwadrat, prostokąt, trójkąt)
# i poda jej pole powierzchni na podstawie wprowadzonych przez użytkownika wartości (długości boków).

class Kwadrat:

    def __init__(self, a):
        self.a = a

    def pole(self):
        return f"Pole kwadratu: {self.a * self.a}"


class Prostokat:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return f"Pole prostokąta: {self.a * self.b}"


class Trojkat:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def pole(self):
        p = (self.a + self.b + self.c) / 2
        return f"Pole Trójkąta: {math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))}"

troj = Trojkat(3,4,5)
print(troj.pole())


