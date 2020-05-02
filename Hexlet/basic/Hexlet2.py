# Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару,
# значения которой расположенны строго в порядке возрастания.


def sort_pair(in_tuple):
    if in_tuple[0] > in_tuple[1]:
        in_tuple = (in_tuple[1], in_tuple[0])

    return in_tuple


print(sort_pair((5, 1)))
