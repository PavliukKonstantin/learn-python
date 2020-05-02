# Вам предстоит реализовать декоратор, добавляющий функции мемоизацию.
# Мемоизация — это запоминание уже вычисленных результатов,
# для уже однажды встреченных аргументов.
#
# Для простоты будем считать, что мемоизироваться будут численные функции
# одного аргумента (аргумент — число, результат — тоже число).
#
# Примеры
# >>> @memoized
# ... def f(x):
# ...     print('Calculating...')
# ...     return x * 10
# ...
# >>> f(1)
# Calculating...
# 10
# >>> f(1)
# 10
# >>> f(42)
# Calculating...
# 420
# >>> f(42)
# 420
# Заметьте, что для каждого нового аргумента выводится сообщение
# "Calculating...", но только лишь один раз.


def memoized(function):
    memory_dict = {}

    def inner(argument):
        memoized_result = memory_dict.get(argument)
        if memoized_result is None:
            memoized_result = function(argument)
            memory_dict[argument] = memoized_result
        return memoized_result

    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
print(f(1))

# @memoized
# def f(x):
#     print('Calculating...')
#     return x * 10
#
#
# def test_memoized():
#     counter = [0]
#
#     @memoized
#     def xor(byte):
#         counter[0] += 1
#         return 255 ^ byte
#
#     assert xor(xor(42)) == 42
#     assert counter == [2], "At this moment xor should be called twice"
#
#     assert xor(42) + xor(xor(42)) == 255
#     assert counter == [2], "No extra xor calls should be happened"
#
#     assert xor(127) == 128
#     assert xor(128) == 127
#     assert counter == [4], "Total number of calls should be four"
#
#
# test_memoized()
