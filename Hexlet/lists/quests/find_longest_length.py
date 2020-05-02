# Реализуйте функцию find_longest_length, принимающую на вход строку и возвращающую длину максимальной
# последовательности из неповторяющихся символов. Подстрока может состоять из одного символа.
# Например в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной будет weqrty,
# а её длина — 6 символов.

# def unique_sequence_length(string):
#     unique_sequence = set()
#     length = 0
#     for char in string:
#         if char in unique_sequence:
#             break
#         unique_sequence.add(char)
#         length += 1
#     return length
#
#
# def find_longest_length(string):
#     longest_length = 0
#     for i, _ in enumerate(string):
#         substring_length = unique_sequence_length(string[i:])
#         if longest_length < substring_length:
#             longest_length = substring_length
#     return longest_length


def find_longest_length(string):
    if not string:
        return 0
    result = []
    for i in range(len(string)):
        temp = []
        for length in string[i:]:
            if length in temp:
                break
            temp.append(length)
        result.append(''.join(temp))
    return len(max(result, key=len))


def test_find_length_length():
    assert find_longest_length('') == 0
    assert find_longest_length('a') == 1
    assert find_longest_length('jabjcdel') == 7
    assert find_longest_length('abcddef') == 4
    assert find_longest_length('abbccddeffg') == 3
    assert find_longest_length('abcd') == 4
    assert find_longest_length('1234561qweqwer') == 9


test_find_length_length()
