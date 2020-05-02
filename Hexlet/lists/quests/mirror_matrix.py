# Реализуйте функцию mirror_matrix, которая принимает двумерный список (матрицу) и возвращает список,
# изменённый таким образом, что правая половина матрицы становится зеркальной копией левой половины,
# симметричной относительно вертикальной оси матрицы. Для простоты условимся, что матрица всегда
# имеет чётное количество столбцов и количество столбцов всегда равно количеству строк.


def mirror_matrix(matrix):
    half_row = len(matrix) // 2
    return [row[:half_row] + row[:half_row][::-1] for row in matrix]


number_sample = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]

b = [row[:(len(row) // 2)] + row[:(len(row) // 2)][::-1] for row in number_sample]

print(b)

empty_sample = [
    [],
]

text_sample = [
    ['he', 'xl', 'et', 'io'],
    ['in', 'my', 'hea', 'rt'],
    ['fo', 're', 've', 'r'],
    ['an', 'd', 'ev', 'er'],
]

number_sample = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]


def test_mirror_matrix():
    assert mirror_matrix(empty_sample) == [[]]
    assert mirror_matrix(text_sample) == [
        ['he', 'xl', 'xl', 'he'],
        ['in', 'my', 'my', 'in'],
        ['fo', 're', 're', 'fo'],
        ['an', 'd', 'd', 'an'],
    ]
    assert mirror_matrix(number_sample) == [
        [11, 12, 13, 13, 12, 11],
        [21, 22, 23, 23, 22, 21],
        [31, 32, 33, 33, 32, 31],
        [41, 42, 43, 43, 42, 41],
        [51, 52, 53, 53, 52, 51],
        [61, 62, 63, 63, 62, 61],
    ]


test_mirror_matrix()
