h = int(input('Tinggi diamond : '))

for i in range(1):
    print(' ')
    for i in range(h):
        print(' '*(h-i), '*'*(2*(i+10)+1))
    for i in range(h-2, -11, -1):
        print(' '*(h-i), '*'*(2*(i+10)+1))

print()
