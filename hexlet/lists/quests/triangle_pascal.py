# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
# В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
# Строки треугольника симметричны относительно вертикальной оси.
# Напишите функцию triangle, которая возвращает указанную строку треугольника паскаля в виде массива.

# from operator import add
#
#
# def triangle(row_number):
#     row = [1]
#     for _ in range(row_number):
#         row = list(map(   # [x,y,z]
#             add,
#             row + [0],    # x y z 0
                            # + + + +
#             [0] + row,    # 0 x y z
#         ))
#     return row


def triangle(line_number):
    paper = []
    while line_number >= 0:
        old_paper = paper
        for index, _ in enumerate(paper):
            if index < len(old_paper) - 1:
                paper[index] = old_paper[index] + old_paper[index + 1]
        paper.insert(0, 1)
        line_number -= 1
    return paper


print(triangle(10))
