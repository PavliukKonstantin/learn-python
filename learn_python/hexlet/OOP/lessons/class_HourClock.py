# Реализуйте класс HourClock, который будет изображать часы с одной лишь
# часовой стрелкой. Текущее время (час) должно сообщать свойство hours.
# Это же свойство должно позволять изменять положение часовой стрелки
# (посредством сеттера). При изменении положения стрелки нужно контролировать,
# чтобы значение оставалось в диапазоне 0..11 (часов).
#
# Примеры
# >>> clock = HourClock()
# >>> clock.hours
# 0
# >>> # в начале часовая стрелка всегда на нуле
# >>>
# >>> clock.hours += 5
# >>> # ^ эквивалентно clock.hours = clock.hours + 5
# >>> clock.hours += 5
# >>> clock.hours
# 10
# >>> clock.hours += 5
# >>> clock.hours
# 3
# >>> clock.hours -= 4
# >>> clock.hours
# 11
# >>> clock.hours = 123
# >>> clock.hours
# 3


class HourClock:  # noqa: WPS306
    def __init__(self, hour=0):
        """Creates an hour clock."""
        self.hour = hour

    @property
    def hours(self):
        return self.hour

    @hours.setter
    def hours(self, change_time):
        self.hour = change_time
        self.hour %= 12


def test_clock():
    clock = HourClock()
    assert clock.hours == 0
    clock.hours += 6
    clock.hours += 5
    assert clock.hours == 11
    clock.hours += 4
    assert clock.hours == 3
    clock.hours -= 4
    assert clock.hours == 11
    clock.hours = 123
    assert clock.hours == 3
