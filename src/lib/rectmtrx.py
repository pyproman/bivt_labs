def chkrectmtrx(mtrx: list[list[float | int]]) -> None:
    """
    Проверяет матрицу на тип и прямоугольность
    """
    if not isinstance(mtrx, list):
        raise TypeError('Matrix is not a list')

    lengths = set()

    for i in mtrx:
        if not isinstance(i, list):
            raise TypeError('Matrix row is not a list')
        lengths.add(len(i))
        for j in i:
            if not (isinstance(j, float) or isinstance(j, int)):
                raise TypeError('Matrix element is not a float or int')
    if len(lengths) > 1:
        raise ValueError('Matrix is not rectangular')
