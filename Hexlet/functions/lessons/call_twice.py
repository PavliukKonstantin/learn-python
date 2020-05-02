# Вам предстоит реализовать функцию call_twice, которая должна
#
# принять функцию и произвольный набор аргументов для неё,
# вызвать функцию с заданными аргументами дважды,
# вернуть пару из результатов вызовов (первый, затем второй).
# Пример использования:
#
# >>> call_twice(input, 'Enter value: ')
# Enter value: foo
# Enter value: bar
# ('foo', 'bar')


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def call_twice(function, *args, **kwargs):
    first = function(*args, **kwargs)
    second = function(*args, **kwargs)
    return first, second


# print(call_twice(shoot))
# print(call_twice(test, value1=24, value2=25))
# print(call_twice(push_and_count, [], value=42))

def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def test_call_twice():
    assert call_twice(push_and_count, [], value=42) == (1, 2), (
        "Function should be called twice with same arguments!"
    )
    assert call_twice(shoot) == ('Bang!', 'Bang!')


test_call_twice()
