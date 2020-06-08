# Цель данного упражнения — реализовать функцию find_second_index.
# В этом упражнении вам пригодится функция
# find_index, которую вы реализовали в прошлом упражнении.
# Напоминаю, эта функция возвращает индекс первого элемента
# последовательности, равного заданному значению.
# Функция find_second_index же должна возвращать индекс второго
# подходящего элемента в последовательности.
# Если подходящих элементов в последовательности меньше двух
# или же последовательность пуста, нужно всё так же возвращать None.

# def find_second_index(value, items):
#     iterator = iter(items)
#     first = find_index(value, iterator)
#     second = find_index(value, iterator)
#     if second is not None:
#         return first + second + 1


from Lists.lessons import find_index


def find_second_index(elem, iterable):
    cursor = iter(iterable)
    first = find_index.find_index(elem, cursor)
    if first is None:
        return None
    second = find_index.find_index(elem, cursor)
    if second is None:
        return None
    return first + second + 1


print(find_second_index('!', '!!'))
