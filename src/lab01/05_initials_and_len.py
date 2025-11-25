fio = input("ФИО: ")
f, i, o = fio.split()
FIO = f[0].upper() + i[0].upper() + o[0].upper()
print(f"Инициалы: {FIO}.")
fio_len = sum(map(len, (f, i, o))) + 2
print(f"Длина (символов): {fio_len}")
