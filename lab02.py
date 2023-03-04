# 1
zdanie = input('Wpisz zdanie:\n')
sep_z = input('Wpisz separator źródłowy:\n')
sep_d = input('Wpisz separator docelowy:\n')
print(zdanie)

zdanie = zdanie.split(sep_z)
nowezdanie = sep_d.join(zdanie)
print(nowezdanie)

# 2
lipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

# 3
imie = "Marcin"
nazwisko = "Pliszka"
litera_1 = imie[3]
litera_2 = nazwisko[4]
liczba_liter1 = lipsum.count(litera_1)
liczba_liter2 = lipsum.count(litera_2)
print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')

# 4
print(f'{"LEWO" :<15}')
print(f'{"ŚRODEK" :^15}')
print(f'{"PRAWO" :>15}')
print(f'{"UTNIJ_DO_5" :.5}')
print(f'{10 :05d}')
print(f'{12 :=+20d}')
data = {'first': 'Abra', 'second': 'Kadabra', 'third': 'Alakazam'}
print(f'{data["first"]} {data["second"]} {data["third"]}!')
