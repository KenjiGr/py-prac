from ast import arg
from audioop import mul
from cmath import sqrt
from time import sleep


name = 'kenji'
age = 20
age += 1

# name = input('Name: ')
# print('welcome '+ name)
# print(float(age))
#print(name + ' is ' + str(age))
# print(name.replace('n', 'm'))

# rows = int(input('Rows: '))
# col = int(input('Columns: '))
# sym = input('Symbol: ')

# for i in range(rows):
#     for j in range(col): 
#         print(sym, end='')
#     print()

phone = '910-546-1102'

for i in phone:
    if i == '-':
        continue
    # print(i, end='')

# if(name[0].islower()):
#     print('is lowercase')

def root(x):
    return sqrt(x)

# print(root(12))

#nested funtion
# print(round(abs(float(input('Enter a number: ')))))

def multiply(*args):
    num = args[0]
    for i in args[1::]:
        num *= i
    return num

# print(multiply(3,4,9))

def hello(**args):
    print('Hello', end=' ')
    for key,value in args.items():
        print(value, end=' ')

# hello(first='kenji', last='greene')