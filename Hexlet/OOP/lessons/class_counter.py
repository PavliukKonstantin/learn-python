# Реализуйте класс Counter, представляющий собой счётчик,
# хранящий неотрицательное целочисленное значение и позволяющий
# это значение изменять:
#
# атрибут value должен хранить текущее значение счётчика (вначале равное нулю),
# метод inc(delta=1) должен увеличивать текущее значение на delta единиц
# (на 1 по умолчанию),
# метод dec(delta=1) должен уменьшать текущее значение на delta единиц.
# Пример
# >>> c = Counter()
# >>> c.inc()
# >>> c.inc()
# >>> c.inc(40)
# >>> c.value
# 42
# >>> c.dec()
# >>> c.dec(30)
# >>> c.value
# 11
# >>> c.dec(delta=100)
# >>> c.value
# 0
# Подсказки
# Пока не обращайте внимание (заглушите) предупреждения WPS306 и WPS601.
# Первое касается наследования, а эта тема будет рассмотрена позже.
# Второе касается переопределения атрибута класса в экземпляре,
# что как правило не рекомендуется, но пока мы умеем инициализировать
# значения атрибутов только таким образом
# (позже вы научитесь и это делать правильно).


class Counter:  # noqa: WPS306
    value = 0

    def inc(self, delta: int = 1) -> None:  # noqa: WPS601
        self.value += delta

    def dec(self, delta: int = 1) -> None:  # noqa: WPS601
        self.value -= delta
        if self.value < 0:
            self.value = 0


def test_counter():
    c = Counter()
    c.inc()
    c.inc()
    c.inc(40)
    assert c.value == 42
    c.dec()
    c.dec(30)
    assert c.value == 11
    c.dec(100)
    assert c.value == 0


def test_counter_independence():
    c1 = Counter()
    c2 = Counter()
    c1.inc(10)
    c2.inc(20)
    assert c1.value == 10
    assert c2.value == 20


test_counter()
test_counter_independence()
