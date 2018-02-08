# Лабораторная работа №2
from math import cosh, log

x = float(input('Enter x:'))
a = float(input('Enter a:'))

g = -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2))
print('G={}'.format(g))

i = (3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)
if i < 0:
    print('Логорифм от отрицательного числа расчитать не возможно')
else:
    y = log(i)
    print('Y={}'.format(y))

j = (21 * a ** 2 - 34 * a * x + 9 * x ** 2)

if (j > -710.000001) and (j < 710.000001):
     f = cosh(j)
     print('F={}'. format(f))
else:
     print('Значение cosh не может быть вычислено')
