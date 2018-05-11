# Лабораторная работа №7

from math import cosh, log

in_f = open('in.txt')
value = in_f.read()
len = len(value)
print(len)

x = float(input('Enter x:'))
a = float(input('Enter a:'))

while ((3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)) < 0:
    print('Невозможно рассчитать функцию Y с данными значениями переменных')
    x = float(input('Enter x:'))
    a = float(input('Enter a:'))

while ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) < -710.000001) or ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) > 710.000001):
    print('Невозможно рассчитать функцию F с данными значениями переменных')
    x = float(input('Enter x:'))
    a = float(input('Enter a:'))

g = -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2))
y = log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)
f = cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2)

print('G={}'. format(g))
print('Y={}'. format(y))
print('F={}'. format(f))

