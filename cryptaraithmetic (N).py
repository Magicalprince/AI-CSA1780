def crypt_arithmetic():
    """Solve the crypt-arithmetic problem SEND + MORE = MONEY using brute force."""
    print("Solving the crypt-arithmetic problem: SEND + MORE = MONEY")

    # Define possible digits for each letter
    for S in range(1, 10):  # S cannot be zero as it's the leading digit
        for E in range(10):
            for N in range(10):
                for D in range(10):
                    for M in range(1, 10):  # M cannot be zero as it's the leading digit
                        for O in range(10):
                            for R in range(10):
                                for Y in range(10):
                                    # Ensure all letters have unique digits
                                    if len(set([S, E, N, D, M, O, R, Y])) == 8:
                                        # Convert letters to numbers
                                        SEND = 1000 * S + 100 * E + 10 * N + D
                                        MORE = 1000 * M + 100 * O + 10 * R + E
                                        MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

                                        # Check if the equation is satisfied
                                        if SEND + MORE == MONEY:
                                            print(f"Solution found!")
                                            print(f"SEND: {SEND}, MORE: {MORE}, MONEY: {MONEY}")
                                            print(f"S = {S}, E = {E}, N = {N}, D = {D}, M = {M}, O = {O}, R = {R}, Y = {Y}")
                                            return  # Exit once a solution is found

    print("No solution found.")  # If no solution exists (very unlikely)

# Run the function
crypt_arithmetic()
