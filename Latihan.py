print('='*10, 'CATATAN BELANJA', '='*10)
daftar1  = ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
daftar2 = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']

print('='*10, 'Daftar 1', '='*10)
print('Daftar Belanja 1: ', daftar1, '\n')
print('='*10, 'Daftar 2', '='*10)
print('Daftar Belanja 2: ', daftar2, '\n')
print('Jawab dengan angka [1/2]\n1. Rubah Belanjaan\n2. Keluar')
pilihan   = int(input('Masukan Pilihan: '))

if pilihan == 1:
    namaitem1       = input('Masukan nama item ke daftar 1: ')
    index1          = int(input('Masukan index yang ingin dirubah: '))
    namaitem2       = input('Masukan nama item ke daftar 2: ')
    index2          = int(input('Masukan index yang ingin dirubah: '))
    daftar1[index1]  = namaitem1
    daftar2[index2] = namaitem2
    print('')
    print('='*10, 'Daftar 1', '='*10)
    print('Daftar Belanja 1: ', daftar1, '\n')
    print('='*10, 'Daftar 2', '='*10)
    print('Daftar Belanja 2: ', daftar2, '\n')

elif pilihan == 2:
    print('\n')
    print('='*10, 'Daftar 1', '='*10)
    print('Daftar Belanja 1: ', daftar1, '\n')
    print('='*10, 'Daftar 2', '='*10)
    print('Daftar Belanja 2: ', daftar2, '\n')
    
else:
    print('\nCAN NOT PROCESS\nERROR')    
