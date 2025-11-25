from ..lib.test import run


def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Возвращает кортеж с минимумом и максимумом значений списка
    """
    if not len(nums):
        raise ValueError("List is empty")
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список без дубликатов
    """
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """
    Возвращает список, в котором значения из списков в списке
    """
    r = []
    for i in mat:
        if not (isinstance(i, list) or isinstance(i, tuple)):
            raise TypeError("List entry is not a list or tuple")
        r.extend(i)
    return r


if __name__ == "__main__":
    run(lambda: min_max([3, -1, 5, 5, 0]), result=(-1, 5))
    run(lambda: min_max([42]), result=(42, 42))
    run(lambda: min_max([-5, -2, -9]), result=(-9, -2))
    run(lambda: min_max([]), result=ValueError)
    run(lambda: min_max([1.5, 2, 2.0, -3.1]), result=(-3.1, 2))

    run(lambda: unique_sorted([3, 1, 2, 1, 3]), result=[1, 2, 3])
    run(lambda: unique_sorted([]), result=[])
    run(lambda: unique_sorted([-1, -1, 0, 2, 2]), result=[-1, 0, 2])
    run(lambda: unique_sorted([1.0, 1, 2.5, 2.5, 0]), result=[0, 1.0, 2.5])

    run(lambda: flatten([[1, 2], [3, 4]]), result=[1, 2, 3, 4])
    run(lambda: flatten(([1, 2], (3, 4, 5))), result=[1, 2, 3, 4, 5])
    run(lambda: flatten([[1], [], [2, 3]]), result=[1, 2, 3])
    run(lambda: flatten([[1, 2], "ab"]), result=TypeError)
