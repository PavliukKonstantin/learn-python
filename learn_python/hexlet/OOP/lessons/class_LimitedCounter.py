# Вам дан класс Counter, реализующий счётчик с инкрементом и декрементом.
# Вам нужно реализовать класс-потомок LimitedCounter, который будет отличаться
# от Counter тем, что при инициализации будет принимать в качестве аргумента
# лимит — максимальное возможное значение счётчика.
#
# Требования к классу LimitedCounter:
#
# Класс должен максимально использовать методы предка,
# если таковые переопределяет.
# Минимальное значение счётчика Counter — 0, должно оставаться таковым
# и для LimitedCounter.
# Примеры
# >>> counter = LimitedCounter(limit=10)
# >>> counter.inc()
# >>> counter.inc(7)
# >>> counter.value
# 8
# >>> counter.dec(10)
# >>> counter.value
# 0
# >>> counter.inc(7)
# >>> counter.inc(7)
# >>> counter.value
# 10


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


class LimitedCounter(Counter):
    """A simple integral counter, with top limit."""

    def __init__(self, limit: int):
        """Initialize a new counter with zero as starting value
         and top limit."""
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        """Increment counter's value, with top limit."""
        super().inc(amount)
        self.value = min(self.value, self.limit)


# counter = LimitedCounter(limit=10)
# counter.inc()
# counter.inc(7)
# print(counter.value)
#
# # counter = Counter()
# # counter.inc()
# # counter.inc(7)
# # print(counter.value)

def test_counter():
    counter = Counter()
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 14


def test_limitedcounter():
    counter = LimitedCounter(limit=10)
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 10


test_counter()
test_limitedcounter()
