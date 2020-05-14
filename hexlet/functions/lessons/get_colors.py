# В этом упражнении вам нужно будет, используя функцию rgb, реализовать функцию
# get_colors,которая должна вернуть словарь цветов.
# В словаре должны присутствовать ключи 'red', 'green', 'blue'.
# Каждому ключу должен соответствовать результат
# вызова функции rgb со значением 255 для соответствующего ключу аргумента.
# Для построения каждого цвета используйте только один аргумент!

# Пример
# >>> colors = get_colors()
# >>> set(colors.keys()) == {'red', 'green', 'blue'}
# True
# >>> colors['red']
# 'rgb(255, 0, 0)'
# >>> colors['blue']
# 'rgb(0, 0, 255)'


def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


# a = {"red": 1, "green": 2, "blue": 3}
# print(a["red"])
# print(a.get("red"))


def get_colors():
    red = rgb(red=255)
    green = rgb(green=255)
    blue = rgb(blue=255)
    return {"red": red, "green": green, "blue": blue}


# colors = get_colors()
# print(colors["red"])
# print(rgb(red=255))


def test_colors():
    colors = get_colors()
    assert set(colors.keys()) == {'red', 'green', 'blue'}
    assert colors['red'] == rgb(red=255)
    assert colors['green'] == rgb(green=255)
    assert colors['blue'] == rgb(blue=255)


test_colors()
