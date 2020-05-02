# Вам нужно реализовать функцию greet, которая должна принимать несколько имён
# (как минимум одно!)
# и возвращать строку приветствия (см. примеры ниже).
#
# >>> greet('Bob')
# 'Hello, Bob!'
# >>> greet('Moe', 'Mary')
# 'Hello, Moe and Mary!'
# >>> greet(*'ABC')
# 'Hello, A and B and C!'


# def greet(who, *args):
#     names = ' and '.join((who,) + args)
#     return 'Hello, {}!'.format(names)


def greet(name, *args):
    others = ' and '.join(list(args))
    if not others:
        return "Hello, {0}!".format(name)
    return "Hello, {0} and {1}!".format(name, others)


print(greet("1", "2", "3"))
print(greet('Bob'))


def test_greet():
    try:
        greet()
    except TypeError:
        pass  # noqa: WPS420
        # thit exception is expected
    else:
        raise AssertionError('Function must not accept empty arguments!')

    assert greet('Bob') == 'Hello, Bob!'
    assert greet('Bob', 'Ann') == 'Hello, Bob and Ann!'
    assert greet('Bob', 'Ann', 'Moe') == 'Hello, Bob and Ann and Moe!'


test_greet()
