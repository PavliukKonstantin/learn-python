# Напишите функцию diff, которая принимает два угла (int) со значениями в диапазоне от 0 до 360,
# и возвращает наименьшую разницу между ними.


def diff(ang1, ang2):
    return abs(abs(ang1 - ang2) - 360) if abs(ang1 - ang2) > 180 else abs(ang1 - ang2)


print(diff(10, 190))
