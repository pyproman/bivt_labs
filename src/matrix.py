from lib.rectmtrx import chkrectmtrx
from lib.test import run

def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Меняет строки и столбцы в mat местами и возвращает результат (mat не изменяется)

    '''
    chkrectmtrx(mat)
    return [[*i] for i in zip(*mat)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Возвращает список с суммами строк mat
    '''
    chkrectmtrx(mat)
    return [sum(l) for l in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Возвращает список с суммами столбцов mat
    '''
    chkrectmtrx(mat)
    return [sum(i) for i in zip(*mat)]

if __name__ == '__main__':
    run(transpose, [[1, 2, 3]], [[1], [2], [3]])
    run(transpose, [[1], [2], [3]], [[1, 2, 3]])
    run(transpose, [[1, 2], [3, 4]], [[1, 3], [2, 4]])
    run(transpose, [], [])
    run(transpose, [[1, 2], [3]], ValueError)

    run(row_sums, [[1, 2, 3], [4, 5, 6]], [6, 15])
    run(row_sums, [[-1, 1], [10, -10]], [0, 0])
    run(row_sums, [[0, 0], [0, 0]], [0, 0])
    run(row_sums, [[1, 2], [3]], ValueError)

    run(col_sums, [[1, 2, 3], [4, 5, 6]], [5, 7, 9])
    run(col_sums, [[-1, 1], [10, -10]], [9, -9])
    run(col_sums, [[0, 0], [0, 0]], [0, 0])
    run(col_sums, [[1, 2], [3]], ValueError)

