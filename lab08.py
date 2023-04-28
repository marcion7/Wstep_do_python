# zad 1

# test czasu wykonania
from timeit import timeit
import random
setup = """
from array import array
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
"""
stmt1 = """
tab_of_chars = array('u', [random.choice(chars) for _ in range(1_000_000)])
"""
stmt2 = """
list_of_chars = [random.choice(chars) for _ in range(1_000_000)]
"""

print(timeit(stmt1, setup, number=100))
print(timeit(stmt2, setup, number=100))

stmt1 = """
tab_of_ints = array('i', [random.randint(0, 100) for _ in range(1_000_000)])
"""
stmt2 = """
list_of_ints = [random.randint(0, 100) for _ in range(1_000_000)]
"""

print(timeit(stmt1, setup, number=100))
print(timeit(stmt2, setup, number=100))

stmt1 = """
tab_of_longs = array('i', [random.randrange(1000000000) for _ in range(1_000_000)])
"""
stmt2 = """
list_of_longs = [random.randrange(1000000000) for _ in range(1_000_000)]
"""

print(timeit(stmt1, setup, number=100))
print(timeit(stmt2, setup, number=100))

# zad 2

from array import array
from datetime import datetime

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

start = datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)

# wczytujemy ponownie dane do tablicy floatów
tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()

koniec = datetime.now()
array_czas = koniec - start

# i analogiczna operacja dla listy
start = datetime.now()
list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]

koniec = datetime.now()
list_czas = koniec - start

print(f"Czas operacji na tablicy: {array_czas}")
print(f"Czas operacji na liście: {list_czas}")

# zad 3

setup = """
from collections import deque
d = deque(maxlen=1000)
l = [0] * 1000
"""

append_czas = timeit('d.append(0)', setup, number=100)
appendleft_czas = timeit('d.appendleft(0)', setup, number=100)

print(f"Deque append time: {append_czas}")
print(f"Deque appendleft time: {appendleft_czas}")

append_czas = timeit('l.append(0)', setup, number=100)
insert_czas = timeit('l.insert(0, 0)', setup, number=100)

print(f"List append time: {append_czas}")
print(f"List insert time: {insert_czas}")

# zad 4

import csv
from collections import namedtuple

with open('zamowienia_polska.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    pola = next(csv_reader)
    pola = [x.replace(" ", '_') for x in pola]

    rekord = namedtuple('Record', pola)

    records = []
    for row in csv_reader:
        record = rekord(*row)
        records.append(record)

print(records)

# zad 5

def najwieksze10(array):
    sorted_arr = sorted(array, reverse=True)
    k = int(len(array) * 0.1)

    return sorted_arr[:k]

tab = array('f', [random.random() for _ in range(100)])
print(najwieksze10(tab))

# zad 6

from collections import Counter, deque

def deque_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.elements())

kolo_fortuny = deque_kolo_fortuny('A', 'B', 'C', 'A', 'B', 'A', 'D', 'A', 'B', 'D')
print(kolo_fortuny)

# zad 7
import time
import numpy as np

def spinit(kolo):

    ticks = len(kolo)
    waits = np.logspace(0.0, 1.0, num=ticks) / ticks
    target = kolo[-1]
    while kolo[0] != target:
        for tick in range(ticks):
            print(kolo[tick], end='')
            time.sleep(waits[tick])
            print('\r', end='')
        kolo.rotate(1)

kolo_fortuny = deque_kolo_fortuny(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

spinit(kolo_fortuny)




