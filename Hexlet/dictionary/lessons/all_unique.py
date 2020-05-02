# Вам предстоит реализовать функцию all_unique, которая должна
# принимать итератор (в т.ч. и те, которые не перезапускаемые!)
# и возвращать True, если элементы в итераторе не повторяются
# (если элементов нет, то ничего не повторяется!). Пример работы функции:

# def all_unique(iterable):
#     items = list(iterable)
#     return len(items) == len(set(items))


def all_unique(iterable):
    res = set()
    for item in iterable:
        if item in res:
            return False
        res.add(item)
    return True


print(all_unique("lo"))


def test_all_unique():
    assert all_unique(iter([])), "Should work with iterators."
    assert all_unique(iter([1])), (
        "Should handle non-restartable iterators too."
    )
    assert all_unique([])
    assert all_unique("cat")
    assert not all_unique("lol")


test_all_unique()
