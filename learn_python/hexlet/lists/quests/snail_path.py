# Реализуйте функцию snail_path, которая принимает на вход матрицу
# и возвращает список элементов матрицы по порядку следования от левого
# верхнего элемента по часовой стрелке к внутреннему.
# Движение по матрице напоминает улитку:
#
# Примеры:
# >>> from solution import snail_path
# >>> snail_path([[1, 2], [3, 4]])
# [1, 2, 4, 3]
# >>> snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]])
# ['b', 'c', 'a', 11, 0, 'foo', None, '3', True]
# >>>


# def snail_path(matrix):
#     snail_line = []
#     while matrix:
#         snail_line += matrix[0]
#         matrix = list(zip(*matrix[1:]))[::-1]
#     return snail_line


def snail_path(matrix: list) -> list:
    result = []

    while matrix:
        if matrix:
            result.extend(matrix.pop(0))
        result.extend([row.pop(-1) for row in matrix if row])
        if matrix:
            result.extend(matrix.pop(-1)[::-1])
        result.extend([row.pop(0) for row in matrix[::-1] if row])
    return result


print(snail_path([]))
print(snail_path([[1], [2], [3], [4]]))
print(snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
print(snail_path([[1, 2, 3, 4],
                  [12, 13, 14, 5],
                  [11, 16, 15, 6],
                  [10, 9, 8, 7]]))


def test_snail_path():
    assert snail_path([]) == []

    assert snail_path([[]]) == []

    assert snail_path([[0]]) == [0]

    assert snail_path([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    assert snail_path([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    assert snail_path([
        [1, 2],
        [3, 4],
    ]) == [1, 2, 4, 3]

    assert snail_path([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    assert snail_path([
        [None, 0, True],
        [-1, '', False],
        [[], 'foo', object],
    ]) == [None, 0, True, False, object, 'foo', [], -1, '']


test_snail_path()
