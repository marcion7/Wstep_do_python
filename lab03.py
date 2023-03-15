# 1
lista = list(range(1,11))
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)

# 2
lista.extend(lista2)
lista = [0] + lista
print(lista)
listaposort = lista
listaposort.sort(reverse=True)
print(listaposort)

# 3
zdanie = input("Podaj zdanie: ")
unikalne = []
for a in zdanie:
    a = a.lower()
    if(a not in unikalne):
        unikalne.append(a)

unikalne.sort()
print(unikalne)

# 4
months_pl = {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec', 8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}

# 5
months_en = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
months_dict = {'pl': months_pl, 'en': months_en}
print(months_dict['pl'][4])
print(months_dict['en'][4])

# 6
tekst = 'Marianna'
liczba = 1
lista = list(tekst)
slownik = dict.fromkeys(lista, liczba)
print(slownik)

# 7
import string

zdanie = input("Podaj ciąg znaków: ")
zdanie = zdanie.lower()
ile_ascii = 0
ile_digits = 0
for a in zdanie:
    if a in string.ascii_lowercase:
        ile_ascii += 1
    elif a in string.digits:
        ile_digits += 1

proc_ascii = ile_ascii/len(zdanie) * 100
proc_digits = ile_digits/len(zdanie) * 100
print(f'W zdaniu jest {ile_ascii} znaków ze string.ascii_lowercase, co stanowi {proc_ascii}% znaków w zdaniu oraz {ile_digits} znaków ze string.digits co stanowi {proc_digits}% znaków w zdaniu')
