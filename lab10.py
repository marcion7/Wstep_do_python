# 1
import os

def make_dirs(lista):
    for p in lista:
        if not os.path.exists(p):
            os.makedirs(p)
            print(f"Folder '{p}' został utworzony.")
        else:
            print(f"Folder '{p}' już istnieje.")

lista = ['D:/test', 'D:/test/test2', 'D:/test']
make_dirs(lista)

# 2
import csv

def polacz_pliki_txt(folder, plik_csv):
    naglowki = set()
    with open(plik_csv, 'w', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik)
        for podfold, _, pliki in os.walk(folder):
            for p in pliki:
                if p.endswith('.txt'):
                    sciezka_plik = os.path.join(podfold, p)
                    with open(sciezka_plik, 'r', encoding='utf-8') as plik_txt:
                        for l in plik_txt:
                            if l.strip() not in naglowki:
                                naglowki.add(l.strip())
                                writer.writerow([l.strip()])

polacz_pliki_txt('C:/Users/plisz/Documents/Wstep do Python/data_for_lab_10', 'wynik.csv')

# 3
from datetime import datetime
from zoneinfo import ZoneInfo

czas = input("Podaj czas w formacie HH:MM:SS: ")
czas = datetime.strptime(czas, "%H:%M:%S").time()
czas_utc = datetime.combine(datetime.utcnow().date(), czas)

tokyo = czas_utc.astimezone(ZoneInfo("Asia/Tokyo")).strftime("%H:%M:%S")
waszyngton = czas_utc.astimezone(ZoneInfo("America/New_York")).strftime("%H:%M:%S")
sydney = czas_utc.astimezone(ZoneInfo("Australia/Sydney")).strftime("%H:%M:%S")
londyn = czas_utc.astimezone(ZoneInfo("Europe/London")).strftime("%H:%M:%S")

print(f"Czas w Tokio: {tokyo}")
print(f"Czas w Waszyngtonie: {waszyngton}")
print(f"Czas w Sydney: {sydney}")
print(f"Czas w Londynie: {londyn}")

# 4
from datetime import date, timedelta

def podaj_wiek(data_ur):
    dzis = date.today()

    if dzis.month > data_ur.month or (dzis.month == data_ur.month and dzis.day >= data_ur.day):
        wiek = dzis.year - data_ur.year - 1
        mies = dzis.month - data_ur.month
        dni = dzis.day - data_ur.day
    else:
        wiek = dzis.year - data_ur.year
        mies = dzis.month - 1 + 12 - data_ur.month
        if data_ur.day > dzis.day:
            days_lastmonth = (dzis.replace(day=1) - timedelta(days=1)).day
            dni = days_lastmonth - data_ur.day + dzis.day
        else:
            dni = dzis.day - data_ur.day

    nast_ur = date(dzis.year, data_ur.month, data_ur.day)
    if nast_ur < dzis:
        nast_ur.year += 1
    dni_do_ur = (nast_ur - dzis).days

    return f"Dzisiaj masz {wiek} lat, {mies} miesięcy i {dni} dni. Do Twoich kolejnych urodzin pozostało {dni_do_ur} dni."

print(podaj_wiek(date(2000, 11, 24)))

# 5
import pandas as pd

def convert_date_format(input_file, date_col_index, source_format, target_format, output_file):
    df = pd.read_csv(input_file)

    df.iloc[:, date_col_index] = pd.to_datetime(df.iloc[:, date_col_index], format=source_format).dt.strftime(target_format)

    df.to_csv(output_file, index=False)

convert_date_format('wynik_mini.csv', 2, '%Y%m%d', '%Y-%m-%d', 'nowywynik.csv')

