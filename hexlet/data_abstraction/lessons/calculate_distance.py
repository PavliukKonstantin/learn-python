# Реализуйте функцию calculate_distance,
# которая находит расстояние между двумя точками на плоскости:
#
# >>> point1 = [0, 0]
# >>> point2 = [3, 4]
# >>> calculate_distance(point1, point2)
# 5.0


def calculate_distance(p1, p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    p3_x, p3_y = p2_x, p1_y
    return pow((p3_x - p1_x) ** 2 + (p2_y - p3_y) ** 2, 0.5)


# p1 = [-1, -4]
# p2 = [-1, -10]
#
# p1_x, p1_y = p1
# p2_x, p2_y = p2
#
# p3_x, p3_y = [p2_x, p1_y]
#
#
# len_p1_p3 = abs(p3_x - p1_x)
# len_p2_p3 = abs(p2_y - p3_y)
#
# len_p1_p2 = pow(pow(len_p1_p3, 2) + pow(len_p2_p3, 2), 0.5)
#
# print(p3_x, p3_y)
# print(len_p1_p3)
# print(len_p2_p3)
# print(len_p1_p2)

print(calculate_distance([3, 4], [-1, -5]))


def test_points():
    assert calculate_distance([0, 0], [3, 4]) == 5
    assert calculate_distance([-1, -4], [-1, -10]) == 6
    assert calculate_distance([1, 10], [1, 3]) == 7


test_points()
