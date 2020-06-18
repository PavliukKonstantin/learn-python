# Write a function that will solve a 9x9 Sudoku puzzle. The function will
# take one argument consisting of the 2D puzzle array, with the value 0
# representing an unknown square.

# The Sudokus tested against your function will be "easy" (i.e. determinable;
# there will be no need to assume and test possibilities on unknowns) and
# can be solved with a brute-force approach.

puzzle = [[5, 3, 0,  0, 7, 0,  0, 0, 0],
          [6, 0, 0,  1, 9, 5,  0, 0, 0],
          [0, 9, 8,  0, 0, 0,  0, 6, 0],

          [8, 0, 0,  0, 6, 0,  0, 0, 3],
          [4, 0, 0,  8, 0, 3,  0, 0, 1],
          [7, 0, 0,  0, 2, 0,  0, 0, 6],

          [0, 6, 0,  0, 0, 0,  2, 8, 0],
          [0, 0, 0,  4, 1, 9,  0, 0, 5],
          [0, 0, 0,  0, 8, 0,  0, 7, 9],
          ]

right_result = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def find_solution_digits(puzzle):
    solution_digits = {}
    for i, row in enumerate(puzzle):
        for j, elem in enumerate(row):
            if elem == 0:
                numbers = set(range(1, 10))
                square = set()
                start_row = ((i//3) * 3)
                end_row = start_row + 3
                start_elem = ((j//3) * 3)
                end_elem = start_elem + 3
                for row in puzzle[start_row:end_row]:
                    for elem in row[start_elem:end_elem]:
                        square.add(elem)
                numbers -= set(puzzle[i]) | {i[j] for i in puzzle} | square
                if len(numbers) == 1:
                    solution_digits[(i, j)] = numbers
    return solution_digits


def sudoku(puzzle):
    while True:
        solution_digits = find_solution_digits(puzzle)
        if not solution_digits:
            break
        for k, v in solution_digits.items():
            i, j = k
            puzzle[i][j] = v.pop()
    return puzzle


print(sudoku(puzzle) == right_result)
