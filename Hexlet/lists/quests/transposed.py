# Транспонированием матрицы называется операция, при которой столбцы матрицы становятся строками,
# а строки становятся столбцами. Представим некую двумерную матрицу
#
# 1 2 3
# 4 5 6
# 7 8 9
# После транспонирования матрица будет выглядеть так:
#
# 1 4 7
# 2 5 8
# 3 6 9
# Транспонирование производилось по главной диагонали, то есть 1, 5 и 9
# остались на своих местах,
# а сама матрица оказалась как бы повёрнута на 180 градусов относительно
# этой воображаемой диагональной оси.
#
# src/solution.py
# Реализуйте функцию transposed, которая должна принимать матрицу в виде
# списка списков и
# возвращать транспонированную матрицу (новый список списков).
#
# Имейте в виду, что хоть в математике и транспонируют
# строго квадратные матрицы,
# ваша функция transposed должна быть более "всеядной":
# она должна уметь переворачивать и прямоугольные матрицы!
#
# Примеры
# >>> transposed([[1]])
# [[1]]
# >>> transposed([[1, 2], [3, 4]])
# [[1, 3], [2, 4]]
# >>> transposed([[1, 2], [3, 4], [5, 6]])
# [[1, 3, 5], [2, 4, 6]]
# >>> transposed(transposed([[1, 2]])) == [[1, 2]]
# True


# def transposed(matrix):
#     return list(map(list, zip(*matrix)))


def transposed(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print(transposed([[1, 2], [3, 4], [5, 6]]))

SAMPLES = (
    # single cell
    ([[42]], [[42]]),

    # column
    ([
         [1],
         [2],
         [3],
     ], [
         [1, 2, 3],
     ]),

    # row
    ([
         [4, 5, 6],
     ], [
         [4],
         [5],
         [6],
     ]),

    # square matrix
    ([
         [10, 20],
         [30, 40],
     ], [
         [10, 30],
         [20, 40],
     ]),

    # rectangle matrix
    ([
         ['d', 'o'],
         ['r', 'e'],
         ['m', 'i'],
     ], [
         ['d', 'r', 'm'],
         ['o', 'e', 'i'],
     ]),
)


def test_transposed():
    for matrix, result in SAMPLES:
        assert transposed(matrix) == result


def test_transposed_reversibility():
    for matrix, _ in SAMPLES:
        assert transposed(transposed(matrix)) == matrix


test_transposed()
test_transposed_reversibility()
