angka = input('Masukan Angka Pecahan: ')


if angka.isdigit():
    print('Bilangan Bulat')
elif angka.replace('.','',1).isdigit() and angka.count('.') < 2:
    print('Integer')
else:
    print('ERROR')
