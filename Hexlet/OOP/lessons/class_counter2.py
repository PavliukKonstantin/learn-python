# Вам предстоит снова реализовать класс Counter.
# Но на этот раз счётчик будет иммутабельный
# (и всё ещё неотрицательный целочисленный):
# методы inc и dec должны возвращать новый счётчик с изменённым значением.
# Атрибут value всё ещё должен содержать текущее значение.
# В этой реализации вам нужно объявить в классе инициализатор,
# позволяющий задать начальное значение счётчика (атрибут value).
# Если же значение при инстанциировании не будет задано,
# следует принять его равным нулю. Внимание, в самом классе атрибут value
# не должен быть объявлен. Этот атрибут должен добавляться в объект
# в инициализаторе. Методы inc(delta=1) и dec(delta=1) должны возвращать
# новый экземпляр счётчика. Старый же экземпляр не должен изменяться при этом!
#
# Примеры
# >>> c = Counter()
# >>> c.inc().inc(5).dec(2).value
# 4
# >>> d = c.inc(100)
# >>> d.dec().value
# 99
# >>> forty_two = Counter(42)
# >>> forty_two.value
# 42


class Counter:  # noqa: WPS306
    def __init__(self, value: int = 0):
        self.value = value

    def inc(self, delta: int = 1):
        return Counter(self.value + delta)

    def dec(self, delta: int = 1):
        return Counter(max(self.value - delta, 0))


# c = Counter()
# print(c.inc().inc(5).dec(2).value)
#
# d = c.inc(100)
# print(d.dec().value)
# print(d.value)
#
# forty_two = Counter(42)
# print(forty_two.value)


def test_counter():
    c = Counter()
    assert c.inc().inc(5).dec(2).value == 4
    d = c.inc(100)
    assert d.dec().value == 99
    forty_two = Counter(42)
    assert forty_two.value == 42


test_counter()
