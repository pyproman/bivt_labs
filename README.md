# labs

## Лабораторная работа 1

### Задание 1 — Привет и возраст
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![Картинка 1](./images/lab01/01.png)

### Задание 2 — Сумма и среднее
```python
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
print(f'sum={a+b:.2f}; avg={(a+b)/2:.2f}')
```
![Картинка 1](./images/lab01/02.png)

### Задание 3 — Чек: скидка и НДС
```python
price = float(input('Цена: ').replace(',', '.'))
discount = float(input('Скидка: ').replace(',', '.'))
vat = float(input('НДС: ').replace(',', '.'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
![Картинка 1](./images/lab01/03.png)

### Задание 4 — Минуты → ЧЧ:ММ
```python
m = int(input('Минуты: '))
print(f'{m//60}:{m%60:02d}')
```
![Картинка 1](./images/lab01/04.png)

### Задание 5 — Инициалы и длина строки
```python
fio = input('ФИО: ')
f,i,o = fio.split()
FIO = f[0].upper() + i[0].upper() + o[0].upper()
print(f'Инициалы: {FIO}.')
fio_len = sum(map(len, (f,i,o)))+2
print(f'Длина (символов): {fio_len}')
```
![Картинка 1](./images/lab01/05.png)

### Задание 6 — Счёт участников
```python
rows = int(input('in_1: '))
c_ochno = 0
c_zaochno = 0
for i in range(rows):
    f,i, age, ochno = input(f'in_{i+2}: ').split()
    if ochno == 'True':
        c_ochno += 1
    else:
        c_zaochno += 1
print(f'out: {c_ochno} {c_zaochno}')
```
![Картинка 1](./images/lab01/06.png)

### Задание 7 — Декодирование
```python
text = input('in: ')
start = [i.isupper() for i in text].index(True)
second = [i.isdecimal() for i in text].index(True, start) + 1
print(text[start::second-start])
```
![Картинка 1](./images/lab01/07.png)

## Лабораторная работа 2

### Задание 1 — `arrays.py`
```python
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
```
![Картинка 1](./images/lab02/img01.png)

### Задание 2 — `matrix.py`
```python
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

```
![Картинка 1](./images/lab02/img02.png)

### Задание 3 — `tuples.py`
```python
from lib.test import run

def format_record(rec: tuple[str, str, float]) -> str:
    '''
    Возвращает строку из записи (fio: str, group: str, gpa: float).
    Пример: Иванов И.И., гр. BIVT-25, GPA 4.60
    '''
    initials = rec[0].split()
    if len(initials) not in (2, 3):
        raise ValueError('Unsupported initials length')
    fmti = f'{initials[0].title()} {initials[1][0].upper()}.'
    if len(initials) == 3:
        fmti += f'{initials[2][0].upper()}.'
    return f'{fmti}, гр. {rec[1].strip()}, GPA {rec[2]:.2f}'

if __name__ == '__main__':
    run(format_record, ('Иванов Иван Иванович', 'BIVT-25', 4.6), 'Иванов И.И., гр. BIVT-25, GPA 4.60')
    run(format_record, ('Петров Пётр', 'IKBO-12', 5.0), 'Петров П., гр. IKBO-12, GPA 5.00')
    run(format_record, ('Петров Пётр Петрович', 'IKBO-12', 5.0), 'Петров П.П., гр. IKBO-12, GPA 5.00')
    run(format_record, ('  сидорова  анна   сергеевна ', 'ABB-01', 3.999), 'Сидорова А.С., гр. ABB-01, GPA 4.00')
```
![Картинка 1](./images/lab02/img03.png)

