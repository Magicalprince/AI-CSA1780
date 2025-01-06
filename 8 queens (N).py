N = 8

def print_solution(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    if row == N:  # All queens are placed
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_nqueens(board, row + 1):  # Recursively place the next queen
                return True
            board[row][col] = 0  # Remove queen (backtrack)

    return False

# Initialize the board
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_nqueens(board, 0):
    print("No solution exists.")
