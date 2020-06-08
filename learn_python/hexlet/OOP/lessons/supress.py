# Реализуйте декоратор suppress ("подавлять"), который должен перехватывать
# заданное исключение (одно или несколько), если таковое возникнет при вызове
# оборачиваемой функции, и возвращать вместо ошибки заданное значение
# (keyword-only аргумент "or_return", значение по умолчанию — None).
#
# Примеры
# >>> @suppress(ZeroDivisionError, or_return=42)
# ... def foo():
# ...      return 1 // 0
# ...
# >>> foo()
# 42
# >>> @suppress((KeyError, IndexError))
# ... def get_item(key, structure):
# ...      return structure[key]
# ...
# >>> get_item(7, "foo") is None
# True
# >>> get_item('a', {}) is None
# True


def suppress(exeption, *, or_return=None):
    def decorate(func):
        def wrapped_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exeption:
                return or_return

        return wrapped_func

    return decorate


# @suppress(ZeroDivisionError, or_return=42)
# def foo():
#     return 1 // 0
#
#
# print(foo())

def walk(path, structure):
    """Walk down to structure using path."""
    if not path:
        return structure
    key, *rest_path = path
    return walk(rest_path, structure[key])


def test_walk():
    assert walk([0], 'Cat') == 'C'
    assert walk(['a', 1], {'a': ('foo', 'bar')}) == 'bar'
    assert walk(['x', 1, 0], {'x': ('foo', 'bar')}) == 'b'


def test_suppress():
    @suppress(ZeroDivisionError, or_return=0)
    def safe_div(a, *, b):
        return a // b

    assert safe_div(10, b=3) == 3
    assert safe_div(10, b=0) == 0


def test_suppress_walk():
    safe_walk = suppress((KeyError, IndexError))(walk)

    assert safe_walk([1], "") is None
    assert safe_walk(['a'], {}) is None
    assert safe_walk([0, 0, 1], (("?", 100), 200)) is None


test_suppress()
test_suppress_walk()
test_suppress()
