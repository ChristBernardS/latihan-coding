# for i in range(1, 10, 1):
#     print('*'*i)

# angka = int(input('Masukan angka : '))
# for i in range(angka):
#     print('  '*i, ('* '*(angka-i))+('* '*(angka-(i+1))))

for i in range(1, 2):
    for x in range(5, 0, -1):
        print(x-(x-i), end=' ')
        for l in range(2, x+1):
            print('*', l, end= ' ')
        print('')

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

# h = int(input('Masukan tinggi diamond : '))
# for i in range(h):
#     print(' '*(h-i), '*'*(2*(i+10)+1))
# for i in range(h-2, -11, -1):
#     print(' '*(h-i), '*'*(2*(i+10)+1))