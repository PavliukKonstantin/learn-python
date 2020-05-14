# Реализуйте функцию enlarge, которая принимает изображение в виде
# двумерного списка строк и увеличивает его в два раза,
# то есть удваивает каждый символ по горизонтали и вертикали.

# def enlarge(image):
#     output = []
#     for line in image:
#         row = []
#         for pixel in line:
#             # expand horizontally
#             row.extend([pixel, pixel])
#         row = ''.join(row)
#         # expand verticaly
#         output.extend([
#             row,
#             row,
#         ])
#     return output


def enlarge(foo):
    foo = [''.join([(j * 2) for j in i]) for i in foo]
    return [i for i in foo for _ in range(2)]


frame = [
    ' *',
    '# ', ]

# '  **',
# '  **',
# '##  ',
# '##  ',

print(enlarge(['ab', 'cd']))
