# Для задания цветов в HTML и CSS используются числа в шестнадцатеричной
# системе счисления. Чтобы не возникало путаницы в определении системы
# счисления, перед шестнадцатеричным числом ставят символ решетки
# "#", например, #135278. Обозначение цвета (rrggbb) разбивается на
# три составляющие, где первые два символа обозначают красную компоненту
# цвета, два средних — зеленую, а два последних — синюю.
# Таким образом каждый из трех цветов — красный, зеленый и синий — может
# принимать значения от 00 до FF в шестнадцатеричной системе исчисления.
#
# При работе с цветами часто нужно получить отдельные значения красного,
# зеленого и синего (RGB) компонентов цвета в десятичной системе исчисления
# и наоборот. Реализуйте функцию rgb2hex, которая конвертирует цвета
# в соответвующее представление.
#
# Функция rgb2hex принимает 3 параметра (цветые компоненты) и возвращает строку.
# Функция должна работать как с позиционными, так и с именованными аргументами.
#
# Примеры:
# >>> rgb2hex(36, 171, 0);
# '#24ab00'
#
# >>> rgb2hex(r=36, g=171, b=0)
# '#24ab00'


def rgb2hex(r=0, g=0, b=0):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


print(rgb2hex(36, 171, 0))


def test_compose():
    assert rgb2hex(0, 0, 0) == '#000000'
    assert rgb2hex(255, 255, 255) == '#ffffff'
    assert rgb2hex(0, 132, 12) == '#00840c'
    assert rgb2hex(36, 171, 0) == '#24ab00'
    assert rgb2hex(r=84, g=63, b=171) == '#543fab'
    assert rgb2hex(r=247, b=222, g=0) == '#f700de'
    assert rgb2hex(r=198, g=1, b=35) == '#c60123'


test_compose()
