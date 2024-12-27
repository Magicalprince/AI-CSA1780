from collections import deque

# Define the state of the problem
def is_valid_state(M_left, C_left, M_right, C_right):
    # The number of missionaries or cannibals can't be negative
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False
    # There can't be more cannibals than missionaries on either side, unless there are no missionaries
    if (M_left > 0 and M_left < C_left) or (M_right > 0 and M_right < C_right):
        return False
    return True

def bfs():
    # Initial state: (Missionaries left, Cannibals left, Missionaries right, Cannibals right, Boat Position)
    initial_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 3, 3, 1)

    # Queue for BFS, starting with the initial state
    queue = deque([(initial_state, [])])  # (state, path to reach the state)
    visited = set()  # To keep track of visited states
    visited.add(initial_state)

    while queue:
        (M_left, C_left, M_right, C_right, Boat_Position), path = queue.popleft()

        # If we reached the goal state, return the path
        if (M_left, C_left, M_right, C_right, Boat_Position) == goal_state:
            return path

        # Generate possible next states
        if Boat_Position == 0:  # Boat is on the left side
            possible_moves = [
                (M_left - 1, C_left, M_right + 1, C_right, 1),  # Move 1 missionary
                (M_left, C_left - 1, M_right, C_right + 1, 1),  # Move 1 cannibal
                (M_left - 2, C_left, M_right + 2, C_right, 1),  # Move 2 missionaries
                (M_left, C_left - 2, M_right, C_right + 2, 1),  # Move 2 cannibals
                (M_left - 1, C_left - 1, M_right + 1, C_right + 1, 1)  # Move 1 missionary and 1 cannibal
            ]
        else:  # Boat is on the right side
            possible_moves = [
                (M_left + 1, C_left, M_right - 1, C_right, 0),  # Move 1 missionary
                (M_left, C_left + 1, M_right, C_right - 1, 0),  # Move 1 cannibal
                (M_left + 2, C_left, M_right - 2, C_right, 0),  # Move 2 missionaries
                (M_left, C_left + 2, M_right, C_right - 2, 0),  # Move 2 cannibals
                (M_left + 1, C_left + 1, M_right - 1, C_right - 1, 0)  # Move 1 missionary and 1 cannibal
            ]

        # For each possible move, check if it's valid and hasn't been visited
        for new_state in possible_moves:
            if is_valid_state(*new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None  # If no solution is found

# Function to print the solution path
def print_solution(solution):
    if not solution:
        print("No solution found")
        return
    for step in solution:
        print(step)

# Run the BFS to solve the Missionaries and Cannibals problem
if __name__ == "__main__":
    solution = bfs()
    print_solution(solution)
