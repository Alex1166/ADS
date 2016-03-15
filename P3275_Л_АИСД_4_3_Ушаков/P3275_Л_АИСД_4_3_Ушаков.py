# -*- coding: utf-8 -*-

from random import randrange
from math import fabs, sqrt


zero = float('inf')


def show_matrix(matrix):    # функция для аккуратного отображения матрицы
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def build_graph(town_amount):
    graph_towns = [[randrange(0, 99), randrange(0, 99)] for i in range(town_amount)]  # координаты каждого города
    graph_roads = [[round(sqrt((fabs(m[0]-n[0]))**2 + (fabs(m[1]-n[1]))**2), 1) for n in graph_towns]
                   for m in graph_towns]
    graph_roads = [[zero if k == 0 else k for k in l] for l in graph_roads]

    return graph_roads


def find_path(graph_roads):
    path = [0]
    path_length = 0
    next_town = 0

    for p in range(len(graph_roads)):
        graph_roads[p][0] = zero     # запрещаем двигаться к начальному городу

    for road in range(len(graph_roads) - 1):
        min_distance = min(graph_roads[next_town])
        next_town = graph_roads[next_town].index(min_distance)   # записываем индекс ближайшего города
        for p in range(len(graph_roads)):
            graph_roads[p][next_town] = zero     # запрещаем двигаться к ближайшему городу

        path_length += min_distance
        path.append(next_town)

    return path, round(path_length, 1)


def ui():
    try:
        town_amount = int(input('Введите количество городов: '))        # количество городов (точек графа)
        print('Матрица расстояний между городами:')
        graph = build_graph(town_amount)
        show_matrix(graph)
        path, path_length = find_path(graph)
        print('Маршрут:', path)
        print('Общая длина пути:', path_length)

    except ValueError:
        print('Ошибка! Необходимо ввести целое число')
        ui()


if __name__ == '__main__':
    ui()