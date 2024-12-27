from collections import deque

# Define the goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Directions for moving the empty tile: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to convert a 2D list into a tuple for easier comparison and hashing
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Function to find the position of the '0' (empty tile) in the state
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to generate the neighbors of a given state by sliding the tiles
def generate_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # Make a copy of the current state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# Breadth-First Search algorithm to find the shortest path
def bfs(initial_state):
    initial_state_tuple = to_tuple(initial_state)
    goal_state_tuple = to_tuple(goal_state)
    
    # Queue for BFS, stores (current_state, path_to_current_state)
    queue = deque([(initial_state, [])])
    
    # Set to keep track of visited states
    visited = set([initial_state_tuple])
    
    while queue:
        current_state, path = queue.popleft()
        
        # If we reached the goal state, return the path
        if to_tuple(current_state) == goal_state_tuple:
            return path
        
        # Generate all valid neighbors
        for neighbor in generate_neighbors(current_state):
            neighbor_tuple = to_tuple(neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No solution found

# Function to print the puzzle state in a human-readable format
def print_state(state):
    for row in state:
        print(" ".join(str(x) for x in row))
    print()

# Example: Solving an 8-Puzzle problem
if __name__ == "__main__":
    # Define the initial state
    initial_state = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
    
    print("Initial State:")
    print_state(initial_state)
    
    # Solve the puzzle using BFS
    solution = bfs(initial_state)
    
    if solution is None:
        print("No solution found")
    else:
        print("Solution path (states leading to the goal):")
        for step in solution:
            print_state(step)
