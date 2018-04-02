# Лабораторная работа №4
# Массивы(списки)

from math import cosh, log

mas_in = []

mas_in.append(input('Enter x:'))
mas_in.append(input('Enter a:'))

x = float(mas_in[0])
a = float(mas_in[1])

while ((3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)) < 0:
    print('Невозможно рассчитать функцию Y с данными значениями переменных')

    mas_in.clear()
    mas_in.append(input('Enter x:'))
    mas_in.append(input('Enter a:'))

    x = float(mas_in[0])
    a = float(mas_in[1])

while ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) < -710.000001) or ((21 * a ** 2 - 34 * a * x + 9 * x ** 2) > 710.000001):
    print('Невозможно рассчитать функцию F с данными значениями переменных')

    mas_in.clear()
    mas_in.append(input('Enter x:'))
    mas_in.append(input('Enter a:'))

    x = float(mas_in[0])
    a = float(mas_in[1])

g = -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2))
y = log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)
f = cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2)

mas_out = []
mas_out.append('G={}'.format(g))
mas_out.append('Y={}'.format(y))
mas_out.append('F={}'.format(f))

for i in range(len(mas_out)):
    print(mas_out[i])
