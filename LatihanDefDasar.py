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

def panjanglebar():
    panjang = int(input('Masukan Panjang : '))
    lebar = int(input('Masukan Lebar : '))
    return panjang,lebar

def luaspersegi(panjang, lebar):
    return panjang*lebar

while True:
    PANJANG, LEBAR = panjanglebar()
    LUAS = luaspersegi(PANJANG, LEBAR)
    print(f'Luas = {LUAS}')
    isContinue = input('Lanjutkan program? (y/n)')
    if isContinue == 'n':
        break
print('program selesai')