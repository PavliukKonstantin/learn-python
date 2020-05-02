# Реализуйте функцию chunked, которая принимает на вход число и последовательность.
# Число которое задает размер чанка (куска). Функция должна вернуть список, состоящий из чанков указанной размерности.
# При этом список должен делиться на куски-списки, строка — на строки, кортеж — на кортежи!

# def chunked(size, source):
#     result = []
#     index = 0
#     while index < len(source):
#         result.append(source[index:index + size])
#         index += size
#     return result


def chunked(number, items):
    foo = []
    start = 0
    end = number
    times = len(items) // number + 1 if len(items) % number else len(items) // number
    for __ in range(times):
        foo.append(items[start:end])
        start = end
        end += number
    return foo


# a = ('a', 'b', 'c', 'd', 'e', 'f')
#
# print(chunked(7, a))

def test_chunked_list():
    assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
    assert chunked(3, ['e', 'f', 'h', 'i']) == [['e', 'f', 'h'], ['i']]
    assert chunked(4, ['g', 'k', 'l', 'm']) == [['g', 'k', 'l', 'm']]
    assert chunked(4, []) == []
    assert chunked(2, ['n']) == [['n']]


def test_chunked_tuple():
    assert chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
    assert chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
    assert chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
    assert chunked(4, []) == []
    assert chunked(2, ('N',)) == [('N',)]


def test_chunked_str():
    assert chunked(2, 'abcd') == ['ab', 'cd']
    assert chunked(3, 'efhi') == ['efh', 'i']
    assert chunked(4, 'gklm') == ['gklm']
    assert chunked(4, '') == []
    assert chunked(2, 'x') == ['x']


test_chunked_list()
test_chunked_tuple()
test_chunked_str()
