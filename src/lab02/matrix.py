from ..lib.rectmtrx import chkrectmtrx
from ..lib.test import run

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
    return row_sums(transpose(mat))

if __name__ == '__main__':
    run(lambda:transpose([[1, 2, 3]]), result=[[1], [2], [3]])
    run(lambda:transpose([[1], [2], [3]]), result=[[1, 2, 3]])
    run(lambda:transpose([[1, 2], [3, 4]]), result=[[1, 3], [2, 4]])
    run(lambda:transpose([]), result=[])
    run(lambda:transpose([[1, 2], [3]]), result=ValueError)

    run(lambda:row_sums([[1, 2, 3], [4, 5, 6]]), result=[6, 15])
    run(lambda:row_sums([[-1, 1], [10, -10]]), result=[0, 0])
    run(lambda:row_sums([[0, 0], [0, 0]]), result=[0, 0])
    run(lambda:row_sums([[1, 2], [3]]), result=ValueError)

    run(lambda:col_sums([[1, 2, 3], [4, 5, 6]]), result=[5, 7, 9])
    run(lambda:col_sums([[-1, 1], [10, -10]]), result=[9, -9])
    run(lambda:col_sums([[0, 0], [0, 0]]), result=[0, 0])
    run(lambda:col_sums([[1, 2], [3]]), result=ValueError)

