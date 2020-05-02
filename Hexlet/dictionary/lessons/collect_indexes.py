# Цель упражнения — функция collect_indexes. Эта функция должна принимать на вход коллекцию (некий iterator/iterable)
# и возвращать словарь (или подобная ему коллекция!), где ключом будет элемент коллекции, а значением для ключа
# — список индексов коллекции, по которым встречается этот элемент.
import collections


def collect_indexes(iterable):
    res = collections.defaultdict(list)
    for index, item in enumerate(iterable):
        res[item].append(index)
    return dict(res)


print(collect_indexes('hello'))


def test_collect_indexes():
    assert collect_indexes([]) == {}
    assert collect_indexes([1]) == {1: [0]}
    assert collect_indexes([1, 2]) == {1: [0], 2: [1]}  # noqa: WPS200
    assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
    assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}  # noqa: WPS221


test_collect_indexes()