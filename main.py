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


def is_winning_move(player):
    if player == 1:
        announcement = 'Player 1 Won'
    else:
        announcement = 'Player 2 Won'
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            print(announcement)
        return True
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][0] == player:
            print(announcement)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(announcement)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print(announcement)
        return True

board = np.zeros((ROWS, COLUMNS))

game_over = False

Turn = 0

while not game_over:
    if Turn % 2 == 0:
        # Player 1
        row = int(input('Player 1: choose row number (0-2):'))
        col = int(input('Player 1: choose column number (0-2):'))
        if is_valid_mark(row, col):
            mark(row, col, 1)
        else:
            Turn -= 1

        # Player 2
        row = int(input('Player 2: choose row number (0-2):'))
        col = int(input('Player 2: choose column number (0-2):'))
        if is_valid_mark(row, col):
            mark(row, col, 2)
        else:
            Turn -= 1

    Turn += 1

    print(board)
