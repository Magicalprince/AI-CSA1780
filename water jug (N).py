def water_jug_problem():
    """
    Solve the Water Jug Problem using a simple brute-force approach without arguments.
    """
    # Input capacities of the jugs and the desired amount
    X = int(input("Enter the capacity of Jug 1: "))
    Y = int(input("Enter the capacity of Jug 2: "))
    Z = int(input("Enter the desired amount of water: "))

    if Z > max(X, Y):
        print("Not possible to measure Z liters.")  # Z cannot be greater than the largest jug capacity.
        return

    # Store the visited states to avoid repetition
    visited = set()
    steps = []

    # Start with both jugs empty
    jug1, jug2 = 0, 0

    for _ in range(1000):  # Limit iterations to avoid infinite loops
        if (jug1, jug2) in visited:
            continue  # Skip already visited states

        visited.add((jug1, jug2))
        steps.append((jug1, jug2))

        # Check if the goal is achieved
        if jug1 == Z or jug2 == Z:
            print("Steps to solve:")
            for step in steps:
                print(f"Jug 1: {step[0]} liters, Jug 2: {step[1]} liters")
            return

        # Possible actions
        if jug1 < X:  # Fill Jug 1
            jug1 = X
        elif jug2 < Y:  # Fill Jug 2
            jug2 = Y
        elif jug1 > 0:  # Empty Jug 1
            jug1 = 0
        elif jug2 > 0:  # Empty Jug 2
            jug2 = 0

        # Transfer from Jug 1 to Jug 2
        transfer = min(jug1, Y - jug2)
        jug1 -= transfer
        jug2 += transfer

        # Transfer from Jug 2 to Jug 1
        transfer = min(jug2, X - jug1)
        jug2 -= transfer
        jug1 += transfer

    print("No solution found within the limit.")

# Example usage
water_jug_problem()
