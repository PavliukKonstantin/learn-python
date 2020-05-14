# Реализуйте функцию sum_of_intervals, которая принимает на вход список интервалов и возвращает сумму
# всех длин интервалов. В данной задаче используются только интервалы целых чисел от 1 до ∞ , которые представлены
# в виде списков. Первое значение интервала всегда будет меньше, чем второе значение. Например, длина интервала [1, 5]
# равна 4, а длина интервала [5, 5] равна 0. Пересекающиеся интервалы должны учитываться только один раз.


# def sum_of_intervals(intervals):
#     values = []
#     for interval in intervals:
#         for i in range(interval[0], interval[1]):
#             if i not in values:
#                 values.append(i)
#     return len(values)


def sum_of_intervals(source):
    range_list = []
    for i in source:
        if i[0] != i[1]:
            range_list.extend([item for item in range(i[0], i[1])])
    return len(set(range_list))


def test_sum_of_intervals():
    assert sum_of_intervals([[5, 5]]) == 0
    assert sum_of_intervals([[3, 10]]) == 7

    assert sum_of_intervals([
        [1, 2],
        [11, 12],
    ]) == 2

    assert sum_of_intervals([
        [2, 7],
        [6, 6],
    ]) == 5

    assert sum_of_intervals([
        [1, 5],
        [1, 10],
    ]) == 9

    assert sum_of_intervals([
        [1, 9],
        [7, 12],
        [3, 4],
    ]) == 11

    assert sum_of_intervals([
        [7, 10],
        [1, 4],
        [2, 5],
    ]) == 7

    assert sum_of_intervals([
        [1, 5],
        [9, 19],
        [1, 7],
        [16, 19],
        [5, 11],
    ]) == 18

    assert sum_of_intervals([
        [1, 3],
        [20, 25]
    ]) == 7


test_sum_of_intervals()
