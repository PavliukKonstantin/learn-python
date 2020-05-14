# Реализуйте функцию same_parity_filter, которая принимает на вход список и возвращает новый список,
# состоящий из элементов, у которых такая же чётность, как и у первого элемента исходного списка.

# def is_even(number):
#     return number % 2 == 0
#
#
# def same_parity_filter(numbers):
#     if not numbers:
#         return []
#
#     first_number_parity = is_even(numbers[0])
#
#     filtered_numbers = filter(
#         lambda number: is_even(number) == first_number_parity,
#         numbers,
#     )
#
#     return list(filtered_numbers)


def same_parity_filter(sequence):
    if not sequence:
        return []
    if sequence[0] % 2 == 0:
        return [i for i in sequence if i % 2 == 0]
    return [i for i in sequence if i % 2 != 0]


def test_same_parity_filter():
    assert same_parity_filter([5, 0, 1, -3, 10]) == [5, 1, -3]
    assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
    assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
    assert same_parity_filter([10, -1.5, 1.3, -3, 25, -2]) == [10, -2]
    assert same_parity_filter([]) == []


test_same_parity_filter()
