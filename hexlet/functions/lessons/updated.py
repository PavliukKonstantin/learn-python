# Цель данного упражнения — функция updated.
# Эта функция должна принимать словарь в качестве
# единственного позиционного аргумента (обязательного) и произвольное
# кол-во именованных аргументов. Возвращать же функция должна
# новую версию словаря, в котором ключи, соответствующие именованным аргументам,
# должны иметь сопутствующие значения (см.примеры).
#
# Примеры
# >>> d = {'a': 1, 'b': False}
# >>> updated(d, a=2, b=True, c=None)
# {'a': 2, 'b': True, 'c': None}
# >>> d
# {'a': 1, 'b': False}
# >>> updated(d) == d
# True
# >>> updated(d) is d
# False


def updated(dictonary: dict, **kwargs):
    new_dict = dictonary.copy()
    new_dict.update(kwargs)
    return new_dict


# a = {"a": 1, "b": True, "c": None}
#
# a.update({"b": False})
#
# print(a)
# old = {'a': 1, 'b': None, 2: 4}
# print(updated(old, a=2))


def test_updated():
    old = {'a': 1, 'b': None, 2: 4}
    copy_of_old = old.copy()
    assert updated(old) is not old
    assert updated(old, a=2) == {'a': 2, 'b': None, 2: 4}
    assert old == copy_of_old, "Old dict should stay unchanged!"
    assert updated({}, foo='bar', bar=42) == {'foo': 'bar', 'bar': 42}


test_updated()
