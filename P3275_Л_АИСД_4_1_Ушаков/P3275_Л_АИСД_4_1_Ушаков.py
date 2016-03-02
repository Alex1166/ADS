# -*- coding: utf-8 -*-

from math import fabs  # высчитывание модуля числа
from itertools import count
from decimal import Decimal  # для точных расчётов
from time import gmtime, strftime


def num(n):     # вызвращает n-ный член ряда
    return Decimal(((-1) ** n) * (1 / (2 * n + 1)))


def sum_acc(e):     # приближенное значение бесконечной суммы с заданной точностью
    sumOfSeries = 0
    i = 0
    while True:
        if fabs(num(i)) < (10 ** (-e)):
            break
        sumOfSeries = Decimal(sumOfSeries + num(i))
        i += 1
    return sumOfSeries


def ui():
    try:
        e = int(input('Введите требуемую точность вычислений (количество знаков после запрятой):\n'))
        print('Вычисление может занять некоторое время...')
        print('Приближенное значение бесконечной суммы с точностью', (10 ** (-e)), ':\n', sum_acc(e))
    except ValueError:
        print('Необходимо ввести целое число')
        ui()

if __name__ == '__main__':
    ui()
