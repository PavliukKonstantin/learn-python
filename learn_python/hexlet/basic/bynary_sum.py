# Рerror: error in 'egg_base' option: 'src' does not exist or is not a directory
# реализуйте функцию binary_sum, которая принимает на вход два двоичных числа
# (в виде строк) и возвращает их сумму.
# Результат (вычисленная сумма) также должен быть бинарным числом в виде строки.


def binary_sum(first, second):
    first = int(first, 2)
    second = int(second, 2)
    out = format(first + second, 'b')
    return out


print(binary_sum('111', '101'))
