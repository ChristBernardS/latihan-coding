print('========== CATATAN BELANJA ==========')
print('========== Daftar I ==========')
mylist = ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
print('Daftar Belanja 1: ',mylist)
print('')
print('========== Daftar 2 ==========')
myList = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']
print('Daftar Belanja 2: ',myList)
print('')
print('Jawab dengan angka [1/2]')
print('1. Rubah Belanjaan')
print('2. Keluar')
Pilihan = int(input('Masukan Pilihan: '))
if Pilihan == 1:
    namaItem1 = input('Masukan nama item ke daftar 1: ')
    namaIndex1 = int(input('Masukan index yang ingin dirubah: '))
    namaItem2 = input('Masukan nama item ke daftar 2: ')
    namaIndex2 = int(input('Masukan index yang ingin dirubah: '))
    mylist[namaIndex1] = namaItem1
    myList[namaIndex2] = namaItem2
    print('========== Daftar I ==========')
    print('Daftar Belanja 1: ',mylist)
    print('')
    print('========== Daftar 2 ==========')
    print('Daftar Belanja 2: ',myList)

else:
    print('eror')
    

