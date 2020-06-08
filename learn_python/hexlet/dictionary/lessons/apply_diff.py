# Цель упражнения — функция apply_diff. Эта функция принимает два аргумента,
# первым из которых выступает множество,
# которое нужно будет изменять "по месту" (возвращать ничего не нужно).
# Вторым аргументом функция принимает словарь,
# который может содержать ключи 'add' и 'remove' с множествами в
# качестве значений.
# Значения по ключу 'add' нужно добавить в изменяемое множество,
# а значения по ключу 'remove' — убрать из множества.
# Прочие ключи в переданном словаре значения не имеют и
# обрабатываться не должны.
# A, B, C, D = 'abcd'
#
# a = {A, B, C}
# # b = {'add': {C, D}}
# b = {}
# if 'add' in b:
#     a.update(b['add'])
# print(a)


def apply_diff(target: set, source: dict):
    if 'add' in source:
        target.update(source['add'])
    if 'remove' in source:
        target.difference_update(source['remove'])


A, B, C, D = 'abcd'


def test_empty_result():
    assert apply_diff(set(), {}) is None, "Function should not return anything!"


def test_apply_empty_diff():
    target = {A, B, C}
    apply_diff(target, {})
    assert target == {A, B, C}, "Empty diff should not change anything!"


def test_apply_unrelated_dict():
    target = {A, B, C}
    apply_diff(target, {'foo': 'bar', True: False})
    assert target == {A, B, C}, "Unrelated keys should not affect target!"


def test_apply_empty_sets():
    target = {A, B, C}
    apply_diff(target, {'add': set(), 'remove': set()})
    assert target == {A, B, C}, "Empty sets should not affect target!"


def test_apply_addition():
    target = {A, B, C}
    apply_diff(target, {'add': {C, D}})
    assert target == {A, B, C, D}


def test_apply_rejecting():
    target = {A, B, C}
    apply_diff(target, {'remove': {A, B}})
    assert target == {C}


test_apply_addition()
test_apply_empty_diff()
test_apply_empty_sets()
test_apply_rejecting()
test_apply_unrelated_dict()
test_empty_result()
