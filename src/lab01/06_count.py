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
