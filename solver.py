# solver.py

def find_empty(board):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return (row, col)
    return None


def valid(board, candidate, row, col):
    rows, cols = len(board), len(board[0])
    # check row
    for c in range(cols):
        if board[row][c] == candidate and c != col:
            return False
    # check column
    for r in range(rows):
        if board[r][col] == candidate and r != row:
            return False
    # check block
    block_row, block_col = row // 3, col // 3
    for r in range(block_row * 3, block_row * 3 + 3):
        for c in range(block_col * 3, block_col * 3 + 3):
            if board[r][c] == candidate and (r, c) != (row, col):
                return False
    return True


def backtrack(board):
    found = find_empty(board)
    if not found:
        return True
    else:
        row, col = found
    for candidate in range(1, 10):
        if valid(board, candidate, row, col):
            board[row][col] = candidate
            if backtrack(board):
                return True
            board[row][col] = 0
    return False


def print_board(board):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(cols):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


