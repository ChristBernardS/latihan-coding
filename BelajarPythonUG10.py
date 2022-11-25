daftarpesanan = str(input('Masukkan daftar pesanan : '))
daftarpesanan1 = [daftarpesanan]
print(daftarpesanan1)
pesananbaru = str(input('Masukkan pesanan yang ingin ditambahkan : '))
if pesananbaru in daftarpesanan:
    print(pesananbaru.title(), 'sudah berada dalam pesanan.')
else:
    daftarpesanan2 = [daftarpesanan, pesananbaru]
    print(daftarpesanan2)

# bulan = {
#     'bulan31': [1, 3, 5, 7, 8, 10, 12],
#     'bulan30': [4, 6, 9, 11],
#     'bulan28': [2]
# }
# month = int(input('Masukkan bulan (1-12): '))
# if month in bulan['bulan31']:
#     print('Jumlah Hari : 31')
# elif month in bulan['bulan30']:
#     print('Jumlah Hari : 30')
# elif month in bulan['bulan28']:
#     print('Jumlah Hari : 28')
# else:
#     print('1 Tahun hanya terdapat 12 bulan\nUlangi program dan input angka 1-12')

# print('='*10, 'Pilih menu', '='*10)
# print('1. Tambah\n2. Kurang\n3. Kali\n4. Bagi')
# angka1 = int(input('Masukkan angka pertama: '))
# angka2 = int(input('Masukkan angka kedua: '))
# pilihan = int(input('Pilihan anda: '))
# if pilihan == 1:
#     print('Hasil:', angka1+angka2)
# elif pilihan == 2:
#     print('Hasil: ', angka1-angka2)
# elif pilihan == 3:
#     print('Hasil: ', angka1*angka2)
# elif pilihan == 4:
#     print('Hasil: ', angka1/angka2)
# else:
#     print('Menu tidak terdaftar kedalam program\nUlangi program dan input angka 1-4')
