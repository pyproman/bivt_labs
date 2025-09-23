from lib.test import run

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''
    Возвращает кортеж с минимумом и максимумом значений списка
    '''
    if not len(nums):
        raise ValueError('List is empty')
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''
    Возвращает отсортированный список без дубликатов
    '''
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    '''
    Возвращает список, в котором значения из списков в списке
    '''
    r = []
    for i in mat:
        if not (isinstance(i, list) or isinstance(i, tuple)):
            raise TypeError('List entry is not a list or tuple')
        r.extend(i)
    return r

if __name__ == '__main__':
    run(min_max, [3, -1, 5, 5, 0], (-1, 5))
    run(min_max, [42], (42, 42))
    run(min_max, [-5, -2, -9], (-9, -2))
    run(min_max, [], ValueError)
    run(min_max, [1.5, 2, 2.0, -3.1], (-3.1, 2))

    run(unique_sorted, [3, 1, 2, 1, 3], [1, 2, 3])
    run(unique_sorted, [], [])
    run(unique_sorted, [-1, -1, 0, 2, 2], [-1, 0, 2])
    run(unique_sorted, [1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5])

    run(flatten, [[1, 2], [3, 4]], [1, 2, 3, 4])
    run(flatten, ([1, 2], (3, 4, 5)), [1, 2, 3, 4, 5])
    run(flatten, [[1], [], [2, 3]], [1, 2, 3])
    run(flatten, [[1, 2], 'ab'], TypeError)
