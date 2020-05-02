# Цель упражнения состоит в реализации цветовой модели RGB в виде класса
# с именем… RGB! Класс должен объявлять три атрибута: red, green и blue,
# имеющие по умолчанию значение 0. Также вам нужно будет объявить в модуле
# переменные red, green и blue, ссылающиеся каждая на свой экземпляр класса RGB.
# При этом у объекта в red атрибут red должен быть равен 255.
# Тем же образом нужно модифицировать и объекты в blue и green.
#
# В итоге всё должно сложиться так, чтобы этот пример заработал:
#
# >>> import solution
# >>> def rgb2tuple(rgb):
# ...     if isinstance(rgb, solution.RGB):
# ...          return None
# ...      return rgb.red, rgb.green, rgb.blue
# ...
# >>> rgb2tuple(42)
# >>> rgb2tuple(solution.red)
# (255, 0, 0)
# >>> rgb2tuple(solution.green)
# (0, 255, 0)
# >>> rgb2tuple(solution.blue)
# (0, 0, 255)
# Подсказки
# Пока мы не умеем наследовать классы, заглушайте сообщение линтера про
# "class without a base class" с помощью комментария # noqa: WPS306.


class RGB:  # noqa: WPS306
    red = 0
    green = 0
    blue = 0


red = RGB()
red.red = 255
green = RGB()
green.green = 255
blue = RGB()
blue.blue = 255


def rgb2tuple(rgb):
    if not isinstance(rgb, RGB):
        return None
    return rgb.red, rgb.green, rgb.blue


rgb2tuple(42)
print(isinstance(red, RGB))
print(rgb2tuple(red))

print(rgb2tuple(green))

print(rgb2tuple(blue))

# def rgb2tuple(rgb):
#     return rgb.red, rgb.green, rgb.blue
#
#
# def test_instances():
#     assert isinstance(solution.red, solution.RGB)
#     assert isinstance(solution.green, solution.RGB)
#     assert isinstance(solution.blue, solution.RGB)
#
#
# def test_attributes():
#     assert rgb2tuple(solution.red) == (255, 0, 0)
#     assert rgb2tuple(solution.green) == (0, 255, 0)
#     assert rgb2tuple(solution.blue) == (0, 0, 255)
