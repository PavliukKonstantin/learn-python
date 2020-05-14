# Реализуйте функцию merged, которая объединяет несколько словарей
# в один общий словарь. Функция принимает любое количество аргументов
# и возвращает результат в виде словаря, в котором каждый ключ содержит
# множество (set) уникальных значений.
#
# Примеры
# >>> from solution import merged
# >>> merged({}, {}) == {}
# True
# >>> merged(
# ...     {'a': 1, 'b': 2},
# ...     {'b': 10, 'c': 100}
# ... ) == {'a': {1}, 'b': {2, 10}, 'c': {100}}
# ...
from copy import deepcopy


def merged(*branches: dict) -> dict:
    result = {}
    for branch in branches:
        for key in branch:
            if key not in result:
                result[key] = set()
            result[key].add(branch.get(key))
    return result


print(merged({'a': 1, 'b': 2}, {'b': 10, 'c': 100}))

A, B, C, D = 'abcd'


def test_merged():

    assert merged() == {}

    assert merged({}, {}) == {}

    assert merged(
        {A: 1},
        {B: 2},
        {C: 3},
    ) == {
        A: {1},
        B: {2},
        C: {3},
    }

    assert merged(
        {A: 1},
        {A: 2},
        {A: 3},
    ) == {
        A: {1, 2, 3},
    }

    assert merged(
        {A: 1, B: 2},
        {B: 3, C: 4},
        {C: 5, D: 6},
    ) == {
        A: {1},
        B: {2, 3},
        C: {4, 5},
        D: {6},
    }

    dict1 = {A: 1, B: 2}
    dict2 = {B: 3, C: 4}
    dict1_copy = deepcopy(dict1)
    dict2_copy = deepcopy(dict2)
    assert merged(
        dict1, dict2,
    ) == {
        A: {1},
        B: {2, 3},
        C: {4},
    }
    assert dict1 == dict1_copy
    assert dict2 == dict2_copy


test_merged()
