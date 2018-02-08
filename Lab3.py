# Лабораторная работа №3
#
# i = 1
#
# print('Введите цифру 1 для выполнения цикла while, и цифру 2 для выполнения цикла for')
# x = int(input('Введите цифру:'))
# y = int(input('Укажите требуемое колличество итераций:'))
#
# if x == 1:
#     while i <= y:
#         i += 1
#     print('Цикл while выполнен {} раз'.format(i))
#
# elif x == 2:
#     for i in range(y):
#         i += 1
#     print('Цикл for выполнен {} раз'.format(i))
#
# else:
#     print('Введено неверное значение')


from math import cosh, log

x = float(input('Enter x:'))
a = float(input('Enter a:'))

f1 = 0
f2 = 0
while f1 == 0:
    i = (3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1) / log(10)
    if i < 0:
        print('Невозможно рассчитать функцию Y с данными значениями переменных')
        x = float(input('Enter x:'))
        a = float(input('Enter a:'))
    else:
        f1 = 1

while f2 == 0:
    j = (21 * a ** 2 - 34 * a * x + 9 * x ** 2)
    if (j < -710.000001) or (j > 710.000001):
        print('Невозможно рассчитать функцию F с данными значениями переменных')
        x = float(input('Enter x:'))
        a = float(input('Enter a:'))
    else:
        f2 = 1

g = -(10 * (18 * a ** 2 + 11 * a * x - 24 * x ** 2) / (-a ** 2 + a * x + 6 * x ** 2))
y = log(i)
f = cosh(j)
print('G={}'. format(g))
print('Y={}'. format(y))
print('F={}'. format(f))

