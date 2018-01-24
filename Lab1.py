# Лабораторная работа №1
# Вариант 20
from math import cosh, log

x = float(input('Enter x:'))
a = float(input('Enter a:'))

g = -(10*(18*a**2+11*a*x-24*x**2)/(-a**2+a*x+6*x**2))
f = cosh(21*a**2-34*a*x+9*x**2)
y = (log(3*a**2-25*a*x+8*x**2+1))/log(10)
print('G={}'. format(g))
print('F={}'. format(f))
print('Y={}'. format(y))
