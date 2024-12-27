from collections import deque

# Directions for moving (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(maze, visited, x, y):
    # Check if the position is within bounds and not a wall or already visited
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and not visited[x][y]

def bfs(maze, start, end):
    # Initialize a queue for BFS
    queue = deque([(start[0], start[1], [])])  # (x, y, path to reach this point)
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]  # Visited cells
    visited[start[0]][start[1]] = True

    while queue:
        x, y, path = queue.popleft()

        # If we reached the end, return the path
        if (x, y) == end:
            return path + [(x, y)]

        # Explore neighbors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, path + [(x, y)]))  # Add new position to the queue

    return None  # No path found

# Example maze
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]

start = (0, 0)  # Start at (0, 0)
end = (3, 4)    # End at (3, 4)

# Run BFS to find the shortest path
path = bfs(maze, start, end)

if path:
    print("Shortest path found:", path)
else:
    print("No path found")
