# Реализуйте функцию is_continuous_sequence, которая проверяет, является ли переданная последовательность целых чисел
# возрастающей непрерывно (не имеющей пропусков чисел). Например, последовательность [4, 5, 6, 7] — непрерывная,
# а [0, 1, 3] — нет. Последовательность может начинаться с любого числа. Главное условие — отсутствие пропусков чисел.
# Последовательность из одного числа не может считаться возрастающей.

# def is_continuous_sequence(source):
#     if len(source) < 2:
#         return False
#     for x, y in zip(source, source[1:]):
#         if (y - x) != 1:
#             return False
#     return True


def is_continuous_sequence(sequence):
    if len(sequence) >= 2:
        for index, __ in enumerate(sequence):
            if sequence[index] + 1 != sequence[index + 1]:
                return False
            if index == len(sequence) - 2:
                break
        return True


def test_is_continuous_sequence():
    assert not is_continuous_sequence([])
    assert not is_continuous_sequence([7])
    assert not is_continuous_sequence([5, 3, 2, 8])
    assert not is_continuous_sequence([10, 11, 12, 14, 15])
    assert not is_continuous_sequence([10, 11, 11, 12])
    assert is_continuous_sequence([0, 1, 2, 3])
    assert is_continuous_sequence([-5, -4, -3])
    assert is_continuous_sequence([10, 11, 12, 13])


test_is_continuous_sequence()
