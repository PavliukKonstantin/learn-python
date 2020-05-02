# В этом упражнении вам предстоит попрактиковаться в использовании
# встроенных функций map, filter, reduce (эту нужно импортировать из functools).
# На их основе вам нужно реализовать три функции: keep_truthful, abs_sum и walk.
#
# keep_truthful
# Эта функция должна принимать на вход итерируемый источник значений и
# возвращать итератор, отдающий только те значения из источника,
# которые "истинны" (вам пригодится функция operator.truth).
#
# Пример использования:
#
# >>> list(keep_truthful([True, False, "", "foo"]))
# [True, 'foo']
# >>>
# abs_sum
# Функция abs_sum принимает на вход итерируемый источник чисел.
# Вернуть же функция должна сумму абсолютных значений этих чисел
# (используйте sum и abs).
#
# Примеры использования:
#
# >>> abs_sum([-3, 7])
# 10
# >>> abs_sum([])
# 0
# >>> abs_sum([42])
# 42
# >>>
# walk
# walk должна для некоего словаря с глубокой вложенностью уметь доставать
# значение по указанному в виде iterable строк пути. В решении можете
# использовать функцию operator.getitem.
#
# Имейте в виду: мы считаем, что значения по указанному пути всегда доступны
# и сама структура словаря всегда правильная. Это означает, что заранее
# обрабатывать ошибки не нужно. Так что реализуйте "оптимистичное решение".
#
# Пример использования:
#
# >>> walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])
# 42
# >>> walk({'a': {7: {'b': 42}}}, ["a", 7])
# {'b': 42}
# >>>
import functools
import operator


def keep_truthful(source):
    return filter(None, source)


print(list(keep_truthful([True, False, "", "foo"])))


def abs_sum(source):
    return sum(map(abs, source))


print(abs_sum([-3, 7]))


# def walk(source: dict, desired):
#     res = source.copy()
#     for elem in desired:
#         res = res.get(elem)
#     return res


def walk(source: dict, desired):
    for elem in desired:
        source = source.get(elem)
    return source


print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))
print(walk({'a': {7: {'b': 42}}}, ["a", 7]))

FALSES = (False, (), None, '', 0)
TRUTHS = (True, (1,), '!', -5)


def test_keep_truthful():
    assert list(keep_truthful(FALSES)) == [], (
        'All falsy values sholud be filtered out!'
    )
    assert list(keep_truthful(TRUTHS)) == list(TRUTHS), (
        'All truthful values sholud be keeped!'
    )
    assert list(keep_truthful([0, 1, 0])) == [1]


def test_abs_sum():
    assert abs_sum([0]) == 0
    assert abs_sum((-42,)) == 42
    assert abs_sum([-3, -2, -1, 0, 1, 2, 3]) == 12  # noqa: WPS221


def test_walk():
    city = {
        'Pine': {
            '5': 'School #42',
        },
        'Elm': {
            '13': {
                '1': 'Appartments #2, Elm st.13',
            },
        },
    }
    assert walk(city, ['Pine', '5']) == city['Pine']['5']
    path = ['Elm', '13', '1']
    assert walk(city, path) == city['Elm']['13']['1']


test_abs_sum()
test_keep_truthful()
test_walk()
