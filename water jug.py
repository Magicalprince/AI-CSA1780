from collections import deque

# Function to perform the BFS for the Water Jug Problem
def water_jug_bfs(x, y, z):
    # Queue to hold the states (water in jug 1, water in jug 2)
    queue = deque()
    visited = set()  # Set to track visited states
    queue.append((0, 0))  # Initial state with both jugs empty
    visited.add((0, 0))  # Mark the initial state as visited

    # List of possible actions: fill, empty, or transfer between jugs
    actions = [
        ("Fill Jug 1", lambda a, b: (x, b)),  # Fill Jug 1
        ("Fill Jug 2", lambda a, b: (a, y)),  # Fill Jug 2
        ("Empty Jug 1", lambda a, b: (0, b)),  # Empty Jug 1
        ("Empty Jug 2", lambda a, b: (a, 0)),  # Empty Jug 2
        ("Pour Jug 1 to Jug 2", lambda a, b: (a - min(a, y - b), b + min(a, y - b))),  # Pour Jug 1 to Jug 2
        ("Pour Jug 2 to Jug 1", lambda a, b: (a + min(b, x - a), b - min(b, x - a)))   # Pour Jug 2 to Jug 1
    ]

    # Perform BFS to find the solution
    while queue:
        a, b = queue.popleft()
        # If we reach the target amount, return the solution
        if a == z or b == z:
            return True

        # Try all possible actions
        for action, move in actions:
            new_a, new_b = move(a, b)
            if (new_a, new_b) not in visited:
                visited.add((new_a, new_b))
                queue.append((new_a, new_b))
    
    return False  # If no solution is found

# Function to print the result
def can_measure_water(x, y, z):
    # If z is greater than the max capacity or z is not a multiple of the GCD of x and y, no solution exists
    from math import gcd
    if z > max(x, y) or z % gcd(x, y) != 0:
        return False
    return water_jug_bfs(x, y, z)

# Example: Jug capacities are 4 and 3 liters, and we need to measure 2 liters
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    if can_measure_water(jug1_capacity, jug2_capacity, target):
        print(f"Yes, it is possible to measure {target} liters using the jugs.")
    else:
        print(f"No, it is not possible to measure {target} liters using the jugs.")
water jug 
