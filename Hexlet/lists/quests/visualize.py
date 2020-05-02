# Реализуйте функцию visualize, которая подсчитывает сколько монет
# каждого номинала есть в копилке и показывает результат в виде графика.
# Каждый столбец графика — стопка монет опредлённого номинала.
#
# Для простоты условимся, что монеты в копилке всегда есть,
# и их количество не ограничено, а номинал может быть любым.
#
# Функция принимает на вход список или кортеж с числами и возвращает
# график в виде строки. Необязательный аргумент bar_char определяет символ,
# с помощью которого рисуется график. Значение по умолчанию — знак рубля (₽).
#
# Для решения используйте встроенный инструмент — Counter.
#
# Примеры
# from solution import visualize
# >>> print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)))
# 5
# ₽₽ 4  4
# ₽₽ ₽₽ ₽₽    3
# ₽₽ ₽₽ ₽₽    ₽₽
# ₽₽ ₽₽ ₽₽ 1  ₽₽
# ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# --------------
# 1  2  3  10 20
# >>>
# >>> print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3), bar_char='$'))
# 5
# $$ 4  4
# $$ $$ $$    3
# $$ $$ $$    $$
# $$ $$ $$ 1  $$
# $$ $$ $$ $$ $$
# --------------
# 1  2  3  10 20

# def visualize(coins, bar_char='₽'):  # noqa: WPS210
#     """Visualize money in a money box."""
#     # BEGIN
#     counts = Counter(coins)
#     nominals = sorted(counts.keys())
#     highest_stack = max(counts.values())
#
#     rows = []
#     delimiter = ''
#
#     for level in range(highest_stack, -1, -1):
#         row = ''
#         for _, bar in sorted(counts.items()):
#             if bar > level:
#                 row += '{} '.format(bar_char * 2)
#             elif bar == level and bar != 0:
#                 row += '{:<2d} '.format(bar)
#                 delimiter += '---'
#             else:
#                 row += '   '
#         rows.append(row[:-1])
#
#     rows.append(delimiter[:-1])
#     row = ''
#     for nominal in nominals:
#         row += '{:<2d} '.format(nominal)
#     rows.append(row[:-1])
#
#     return '\n'.join(rows)


from collections import Counter


def get_max_item(source):
    return max((value for value in source))


def get_max_item_len(source):
    return max((len(str(key)) for key in source))


def item_to_str(item, length):
    return "{0}{1}".format(item, " " * (length - len(str(item))))


# def get_column(key, value, column_width, bar_char):
#     return "{0}-{1}{2}{3}".format(
#         item_to_str(key, column_width)[i],
#         bar_char * value,
#         item_to_str(value, column_width)[i],
#         " " * (max_len_column - value),
#     )


def visualize(coins, bar_char='₽'):
    counted = Counter(coins)
    max_len_column = get_max_item(counted.values())
    column_width = max(
        get_max_item_len(counted.keys()),
        get_max_item_len(counted.values()),
    )

    columns = []
    for key, value in sorted(counted.items()):
        for i in range(column_width):
            columns.append("{0}-{1}{2}{3}".format(
                item_to_str(key, column_width)[i],
                bar_char * value,
                item_to_str(value, column_width)[i],
                " " * (max_len_column - value),
            ))

        if sorted(counted.items())[-1] != (key, value):
            columns.append(" -{0}".format(" " * (max_len_column + 1)))

    return "\n".join(map(''.join, zip(*(column[::-1] for column in columns))))


source1 = (  # noqa: WPS317
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)
print(visualize(source1))
# print("""
#    6
#    ₽₽          5
# 4  ₽₽          ₽₽
# ₽₽ ₽₽          ₽₽
# ₽₽ ₽₽ 2  2  2  ₽₽
# ₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# ₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# -----------------
# 1  2  3  5  10 20
# """[1:-1]
# )


MONEY = (  # noqa: WPS317
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)


def test_visualize():
    assert visualize(MONEY) == """
   6             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2  2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291

    assert visualize(MONEY, bar_char='$') == """
   6             
   $$          5 
4  $$          $$
$$ $$          $$
$$ $$ 2  2  2  $$
$$ $$ $$ $$ $$ $$
$$ $$ $$ $$ $$ $$
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291


test_visualize()
