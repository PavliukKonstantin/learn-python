# Реализуйте следующие функции для работы с точками:
#
# get_quadrant — функция, которая вычисляет квадрант, где находится точка.
# Ниже приведена схема, показывающая номера квадрантов на плоскости.
#
#         +
#       2 | 1
#         |
# +----------------+
#         |
#       3 | 4
#         +
# >>> point1 = points.make(1, 5)
# >>> get_quadrant(point1)
# 1
# >>> point2 = points.make(1, -5)
# >>> get_quadrant(point2)
# 4
# Если точка не принадлежит ни одному квадранту (т.е., если она лежит хотя
# бы на одной из осей координат), то функция должна возвращать None:
#
# >>> point1 = points.make(0, 7)
# >>> get_quadrant(point1) is None
# True
# >>> point2 = points.make(2, 0)
# >>> get_quadrant(point2) is None
# True
# get_symmetrical_point — функция, возвращающая новую точку, симметричную
# относительно начала координат. Такая симметричность означает, что меняются знаки у x и y.
#
# >>> points.to_string(get_symmetrical_point(points.make(1, 5)))
# '(-1, -5)'
# calculate_distance — функция, вычисляющая расстояние между точками по
# формуле: d = √((x₂−x₁)²+(y₂−y₁)²)
#
# >>> calculate_distance(
# ...     points.make(3, 2),
# ...     points.make(-1, -1))
# ... )
# 5.0
# import unittest
import math


def make(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


# ______________________________________________________________________________


def get_quadrant(point):
    x = points.get_x(point)
    y = points.get_y(point)
    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4
    return None


def get_symmetrical_point(point):
    return points.make(-points.get_x(point), -points.get_y(point))


def calculate_distance(point1, point2):
    delta_x = points.get_x(point2) - points.get_x(point1)
    delta_y = points.get_y(point2) - points.get_y(point1)
    return (delta_x ** 2 + delta_y ** 2) ** 0.5

# def test_get_quadrant():
#     for coords, expected in [  # noqa: WPS335
#         [(0, 0), None],
#         [(5, 0), None],
#         [(1, 5), 1],
#         [(-3, 10), 2],
#         [(-2, -5), 3],
#         [(4, -1), 4],
#     ]:
#         quadrant = points.get_quadrant(hexlet.points.make(*coords))
#         assert quadrant == expected
#
#
# def test_get_symmetrical_point():
#     for coords, expected_coords in [  # noqa: WPS335
#         [(10, 10), (-10, -10)],
#         [(-10, -10), (10, 10)],
#         [(10, -10), (-10, 10)],
#     ]:
#         symmetrical_point = hexlet.points.to_string(
#             points.get_symmetrical_point(hexlet.points.make(*coords)),
#         )
#         expected_point = hexlet.points.to_string(
#             hexlet.points.make(*expected_coords),
#         )
#         # for clear error messages
#         # every point should be converted to string!
#         assert symmetrical_point == expected_point
#
#
# class TestCalculateDistance(unittest.TestCase):
#     def test_calculate_distance(self):
#         point1 = hexlet.points.make(-2, -3)
#         point2 = hexlet.points.make(-4, 4)
#         self.assertAlmostEqual(
#             points.calculate_distance(point1, point2),
#             7.28,
#             2,
#         )
