# for i in range(10):
#     print(i+1)

# for x in range(1, 6, 1):
#     print(x, end=' ')
#     for l in range(2, x+1):
#         print(x-l+1, end= ' ')
#     print('')

# num = 2
# for i in range(1, 11):
#     print(num*i)

# number = [12, 75, 150, 180, 145, 525, 50]
# for item in number:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item%5 == 0:
#         print(item)
#     else:
#         print('ERROR')

# for x in range(1, 6, 1):
#     for l in range(5, x-1,-1):
#         print(l, end= ' ')
#     print('')

# list1 = [10, 20, 30, 40, 50]
# for item in list(reversed(sorted(list1))):
#     print(item)

# for i in range(-10, 0):
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print('Done!')

# print('Prime numbers between 25 and 50 are:')
# for num in range(25, 51):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)

# num0, num1 = 0, 1
# print('Fibanoci Sequence')
# for i  in range(10):
#     print(num0, end=' ')
#     newnum = num0 + num1
#     num0 = num1
#     num1 = newnum

# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#     print(i, end=" ")

# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))

# n = 5
# start = 2
# sum_seq = 0
# for i in range(0, n):
#     print(start, end="+")
#     sum_seq += start
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)

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