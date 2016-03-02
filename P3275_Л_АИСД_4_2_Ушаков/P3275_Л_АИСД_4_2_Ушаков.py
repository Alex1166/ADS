# -*- coding: utf-8 -*-

from random import randrange


def convert_matrix(matrix, m):
    for k in range(m):
        for i in range(len(matrix)):            # проход по строкам
            for j in range(len(matrix[i])):     # проход по столбцами
                try:
                    if matrix[i][j] > matrix[i+1][j]:
                        r = matrix[i][j]
                        matrix[i][j] = matrix[i+1][j]
                        matrix[i+1][j] = r
                except IndexError:
                    pass
    return matrix


def show_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def ui():
    try:
        m = int(input('Введите количество строк: '))        # количество строк
        n = int(input('Введите количество столбцов: '))     # количество столбцов
        inputMatrix = [[randrange(0, 99) for cell in range(n)] for line in range(m)]       # генерация матрицы
        print('Строк: {0}\nСтолбцов: {1}\n'.format(m, n))
        print('Исходная матрица:')
        show_matrix(inputMatrix)
        print('\nПреобразованная матрица:')
        show_matrix(convert_matrix(inputMatrix, m))
    except ValueError:
        print('Необходимо ввести целое число')
        ui()


if __name__ == '__main__':
    ui()
