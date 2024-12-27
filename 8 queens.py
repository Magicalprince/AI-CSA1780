def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n, solutions, max_solutions=1):
    # If all queens are placed, add the solution to the list
    if row == n:
        solutions.append(board[:])
        if len(solutions) >= max_solutions:  # Stop if we reach the desired number of solutions
            return True
        return False

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place the queen
            if solve_n_queens(board, row + 1, n, solutions, max_solutions):  # Recur to place the next queen
                return True  # If a solution is found, return immediately
            board[row] = -1  # Backtrack
    return False

def print_solution(board, n):
    # Print the solution in a readable format
    for row in range(n):
        line = ['Q' if board[row] == col else '.' for col in range(n)]
        print(' '.join(line))
    print()

def n_queens(n, max_solutions=1):
    board = [-1] * n  # Initialize the board, -1 indicates no queen placed
    solutions = []  # List to store all solutions
    solve_n_queens(board, 0, n, solutions, max_solutions)
    
    # Print all solutions (up to max_solutions)
    print(f"Total solutions found: {len(solutions)}\n")
    for solution in solutions:
        print_solution(solution, n)

# Solve the 8-Queens problem and stop after finding the first solution
if __name__ == "__main__":
    n = 8
    n_queens(n, max_solutions=1)  # Change max_solutions to a different value to stop after more solutions
