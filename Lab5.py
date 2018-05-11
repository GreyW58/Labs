# Лабораторная работа №5
# Строки

from math import cosh, log

x_str = str(input('Enter x:'))
a_str = str(input('Enter a:'))

x = float(x_str)
a = float(a_str)

while ((3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)) < 0:
    print('Невозможно рассчитать функцию Y с данными значениями переменных')
    x_str = str(input('Enter x:'))
    a_str = str(input('Enter a:'))

    x = float(x_str)
    a = float(a_str)

while ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) < -710.000001) or ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) > 710.000001):
    print('Невозможно рассчитать функцию F с данными значениями переменных')
    x_str = str(input('Enter x:'))
    a_str = str(input('Enter a:'))

    x = float(x_str)
    a = float(a_str)

g = -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2))
y = log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)
f = cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2)

out = str('G={} \n'.format(g) + 'Y={} \n'.format(y) + 'F={} \n'.format(f))

print(out)
