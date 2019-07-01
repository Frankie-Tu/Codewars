'''
Challenge created by xDranik

9 x 9 Sudoku board.
Validate if the solution is valid

Input format:
[
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

Condition:
1. each of the nine 3x3 sub-grids should contain distinct number 1 - 9
2. each row and column should only contain distinct number from 1 - 9

Return boolean:
True/False
'''


def sudoku_validator(board):
    valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # row checking
    for arr in board:
        if sorted(arr) != valid_list:
            return False

    # column checking
    for c in range(0, 9):
        current_column = []
        for r in range(0, 9):
            current_column.append(board[r][c])
        if sorted(current_column) != valid_list:
            return False

    # 3 x 3 sub-grid checking
    x = y = [0, 3, 6]
    for num_x in x:
        for num_y in y:
            if sub_grid_checker(num_x, num_y, board) != valid_list:
                return False

    # all checks passed, return true
    return True


def sub_grid_checker(coord_x, coord_y, board):
    sub_grid_list = []
    for x in range(0, 3):
        for y in range(0, 3):
            sub_grid_list.append(board[coord_x + x][coord_y + y])
    return sorted(sub_grid_list)


myinput = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(sudoku_validator(myinput))
