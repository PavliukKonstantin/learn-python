# В этот раз вы снова будете реализовывать мемоизирующий декоратор "memoizing".
# Но на этот раз декоратор должен принимать аргумент, задающий максимальное
# количество запоминаемых значений. При превышении количества запомненных
# значений лишние должны быть отброшены, причём сначала — самые старые!
#
# Напоминаю, мемоизируемые функции считать численными
# функциями одного аргумента.
# И не забудьте про functools.wraps!
#
# Примеры
# >>> @memoizing(3)
# ... def f(x):
# ...     print('Calculating...')
# ...     return x * 10
# ...
# >>> f(1)
# Calculating...
# 10
# >>> f(1)  # будет "вспомнено"
# 10
# >>> f(2)
# Calculating...
# 20
# >>> f(3)
# Calculating...
# 30
# >>> f(4)  # вытеснит запомненный результат для "1"
# Calculating...
# 40
# >>> f(1)  # будет перевычислено
# Calculating...
# 10
from functools import wraps


def memoizing(memory_len):
    def memoized(function):
        memory_dict = {}

        @wraps(function)
        def inner(argument):
            memoized_result = memory_dict.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                memory_dict[argument] = memoized_result
                if len(memory_dict) > memory_len:
                    memory_dict.pop(tuple(memory_dict.keys())[0])
            return memoized_result

        return inner

    return memoized


@memoizing(2)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
print(f(2))
print(f(3))
print(f(1))


def test_memoizing():
    arguments = []

    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1

    assert inc(inc(inc(0))) == 3
    assert arguments == [0, 1, 2]

    _ = inc(inc(inc(0)))
    assert arguments == [0, 1, 2], "All resluts sholud be got from memory!"

    assert inc(10) == 11
    assert arguments == [0, 1, 2, 10], "New argument should be added!"

    assert inc(0) == 1
    assert arguments == [0, 1, 2, 10, 0], (
        "Result for zero should be recalculated!",
    )


def test_memoizing_wrapping():
    @memoizing(3)
    def foo():
        """Return bar."""

    assert foo.__name__ == "foo", (
        "Wrapper should preserve function's name!",
    )
    assert foo.__doc__ == "Return bar.", (
        "Wrapper should preserve function's docstring!",
    )


test_memoizing()
test_memoizing_wrapping()
