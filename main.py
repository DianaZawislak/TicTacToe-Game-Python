import numpy as np

ROWS = 3
COLUMNS = 3


def mark(row, column, player):
    board[row][column] = player


# this checks if square is empty
def is_valid_mark(row, column):
    return board[row][column] == 0


# this checks if the board is full and game needs to be restarted
def _board_is_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True


board = np.zeros((ROWS, COLUMNS))

print(board)
mark(1, 0, 2)
print(board)
print(is_valid_mark(1, 0))
