# Лабораторная работа №6

from math import cosh, log


class Out(object):
    def __init__(self, name=None,  value=2000):
        self.name = name
        self.value = value
        print(name, value)


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


g = Out('g =', -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2)))
y = Out('y =', log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10))
f = Out('f =', cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2))
