# Реализуйте функцию fib, находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.


# def fib(n):
#     a = 0
#     b = 1
#     string = []
#     for i in range(n):
#         a, b = b, a + b
#     return a

def fib(index):
    if index <= 0:
        return 0
    elif index == 1:
        return 1
    return fib(index - 1) + fib(index - 2)


print(fib(5))


