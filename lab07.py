# 1
from typing import Any


def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, int | float), vals))

a = ['a', 1, '1.53', 4.54242, 5, 'aaa']

print(extract_numbers(a))

# 2
wyrazy = input('Podaj wyrazy: ')
lista_wyr = wyrazy.split()
lista_wyr_sort = sorted(lista_wyr, key=lambda x: len(x), reverse=True)
print(lista_wyr_sort)

# 3
def sortuj_int_i_str(lista, reversed=False):
    sort_int = sorted(list(filter(lambda x: isinstance(x, int), lista)))
    sort_str = sorted(list(filter(lambda x: isinstance(x, str), lista)))
    if reversed == False:
        return sort_int + sort_str
    else:
        return sort_str + sort_int


lista = ['aa', 1, 9, 5, 'vv', 'cc']
print(sortuj_int_i_str(lista, reversed=True))

# 4
import csv
from datetime import date

with open('zamowienia.csv', newline='', encoding='utf-8', errors='replace') as csvfile:
    with open('zamowienia_polska.csv', 'w', newline='') as csvfile_polska:
        with open('zamowienia_niemcy.csv', 'w', newline='') as csvfile_niemcy:
            kolumny = ['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']
            writer_pl = csv.DictWriter(csvfile_polska, fieldnames=kolumny)
            writer_ni = csv.DictWriter(csvfile_niemcy, fieldnames=kolumny)
            writer_pl.writeheader()
            writer_ni.writeheader()
            reader = csv.DictReader(csvfile, delimiter=';')
            razem = list(map(lambda x: {"Kraj": x.get("Kraj"), "Sprzedawca": x.get("Sprzedawca"),
                                        "Data zamowienia": date(int(x.get("Data zamowienia").split('.')[2]), int(x.get("Data zamowienia").split('.')[1]), int(x.get("Data zamowienia").split('.')[0])) if len(x.get("Data zamowienia").split('.')) > 1 else x.get("Data zamowienia").split('.')[0],
                                        "idZamowienia": x.get("idZamowienia"), "Utarg": x.get("Utarg").replace(',', '.').replace(' ', '').split('z')[0]}, reader))
            polska = list(filter(lambda x: x["Kraj"] == "Polska", razem))
            niemcy = list(filter(lambda x: x["Kraj"] == "Niemcy", razem))
            writer_pl.writerows(polska)
            writer_ni.writerows(niemcy)


# 5
def sortuj_slownik(slownik, funkcja):
    if 'abs' in str(funkcja):
        for i in range(len(slownik)):
            for j in range(len(list(slownik.values())[i])-1):
                sort = sorted(slownik.items(), key=lambda x: funkcja(x[1][j]))
    else:
        sort = sorted(slownik.items(), key=lambda x: funkcja(x[1]))
    return dict(sort)


slownik = {'Jan': [3, 5, -4, 13], 'Marek': [7, 6, 4, 5, 10], 'Paweł': [8, 6, -2, 7]}
print(sortuj_slownik(slownik, abs))