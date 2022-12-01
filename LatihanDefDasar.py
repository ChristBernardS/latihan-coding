# def datadiri (name, age):
#     print(name, age)
# datadiri('Ber', 18)


# def x(a, b):
#     return a+b, a-b
# add, sub = x(40, 10)
# print(add, sub)

# def inputuser():
#     '''fungsi input user'''
#     panjang = int(input('Masukan Panjang : '))
#     lebar = int(input('Masukan Lebar : '))
#     return panjang, lebar

# def menghitung(panjang, lebar):
#     return panjang*lebar

# def display(message, value):
#     print(f'{message}={value}')

# while True:
#     PANJANG, LEBAR = inputuser()
#     LUAS = menghitung(PANJANG, LEBAR)
#     display('luas', LUAS)

#     isContinue = input('Apakah ingin lanjut? (y/n)')
#     if isContinue == 'n':
#         break
# print('Program selesai')

# def panjanglebar():
#     panjang = int(input('Masukan Panjang : '))
#     lebar = int(input('Masukan Lebar : '))
#     return panjang,lebar

# def luaspersegi(panjang, lebar):
#     return panjang*lebar

# PANJANG, LEBAR = panjanglebar()
# LUAS = luaspersegi(PANJANG, LEBAR)
# print(f'Luas Persegi : {LUAS}')

print('+'*10, 'PROGRAM KONVERSI SUHU', '+'*10, '\n')
def inputsuhu():
    celcius = int(input('Masukan Skala Celcius: '))
    return celcius

def reamur(celcius):
    return celcius*4/5
def fahrenhent(celcius):
    return (celcius*9/5)+32
def kelvin(celcius):
    return celcius+273

CELCIUS = inputsuhu()
SUHUREAMUR = reamur(CELCIUS)
SUHUFAHRENHEIT = fahrenhent(CELCIUS)
SUHUKELVIN = kelvin(CELCIUS)

print(f'Hasil Konversi Suhu {CELCIUS} C adalah {SUHUREAMUR} Kelvin')
print(f'Hasil Konversi Suhu {CELCIUS} C adalah {SUHUFAHRENHEIT} Kelvin')
print(f'Hasil Konversi Suhu {CELCIUS} C adalah {SUHUKELVIN} Kelvin')