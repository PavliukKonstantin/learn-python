# Цель упражнения — функция count_all. Эта функция должна принимать на
# вход iterable источник и возвращать словарь,
# ключами которого являются элементы источника, а значения отражают
# количество повторов элемента в коллекции-источнике.
# Вот пара примеров, демонстрирующих то, как функция должна работать:

# def count_all(items):
#     counters = {}
#     for item in items:
#         counters[item] = counters.get(item, 0) + 1
#     return counters


def count_all(iterable):
    return {i: iterable.count(i) for i in iterable}


print(count_all("Hello"))


def test_count_all():
    assert count_all([]) == {}
    assert count_all("") == {}
    assert len(count_all("cat")) == 3
    assert len(count_all("foo")) == 2
    assert list(count_all("dog").values()) == [1, 1, 1]
    assert count_all("ololo")["o"] == 3


test_count_all()
