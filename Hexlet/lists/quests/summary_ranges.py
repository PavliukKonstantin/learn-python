# Реализуйте функцию summary_ranges, которая находит в списке непрерывные возрастающие последовательности чисел
# и возвращает список с их перечислением.
#
# Примеры
# >>> summary_ranges([])
# []
# >>> summary_ranges([1])
# []
# >>> summary_ranges([1, 2, 3])
# ['1->3']
# >>> summary_ranges([0, 1, 2, 4, 5, 7])
# ['0->2', '4->5']
# >>> summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])
# ['110->112', '-5->-4']


def summary_ranges(numbers):
    if not numbers:
        return []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]
    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)
    return ["{0}->{1}".format(i[0], i[-1]) for i in sequences if len(i) > 1]


print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5, -2, -1]))

# def summary_ranges(source):
#     res = []
#     temp = []
#     if len(source) < 2:
#         return res
#     for index, x in enumerate(zip(source, source[1:])):
#         if x[1] - x[0] == 1 and not temp:
#             temp.append(x[0])
#             temp.append(x[1])
#         elif x[1] - x[0] == 1 and temp and index < len(source) - 2:
#             temp.append(x[1])
#         elif x[1] - x[0] != 1 and temp:
#             res.append(temp)
#             temp = []
#         elif index == len(source) - 2 and x[1] - x[0] == 1 and temp:
#             temp.append(x[1])
#             res.append(temp)
#             temp = []
#     if temp:
#         res.append(temp)
#     print(res)
#     return ["{0}->{1}".format(i[0], i[-1]) for i in res if len(i) > 1]


# print(summary_ranges([1, 2]))


# def test_find_summary_ranges():
#     assert summary_ranges([]) == []
#     assert summary_ranges([1]) == []
#     assert summary_ranges([1, 2, 3]) == ['1->3']
#     assert summary_ranges([0, 1, 2, 7, 5, 6]) == ['0->2', '5->6']
#     assert summary_ranges(
#         [1, 1, 3, 4, 5, -6, 8, 9, 10, 12, 14, 14],
#     ) == ['3->5', '8->10']
#     assert summary_ranges(
#         [110, 111, 112, 111, -5, -4, -2, -3, -4, -5],
#     ) == ['110->112', '-5->-4']
#
#
# test_find_summary_ranges()
