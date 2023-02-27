#2
base2 = int('110', base=2)
print(base2)
base16 = int('A5F0', base=16)
print(base16)
float_str = float('10')
print(float_str)
float_int = float(12)
print(float_int)

#3
liczba1 = 2.0
print(bin(int(liczba1)))
liczba2 = 3.5
print(bin(int(liczba2)))
print(int(liczba1).bit_count())
print(int(liczba2).bit_count())
print(float.is_integer(liczba1))
print(float.is_integer(liczba2))

#4
print(16>>2) # 10000 >> 100
print(int('1001', base=2) & int('1101', base=2)) # 1001 = 9
print(int('1001', base=2) | int('1101', base=2)) # 1101 = 13
print(int('1001', base=2) ^ int('1101', base=2)) # 0100 = 4