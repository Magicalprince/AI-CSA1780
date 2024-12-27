import itertools

def cryptarithmetic():
    # The letters in the puzzle
    letters = 'SENDMOREMONEY'
    
    # Get all unique permutations of the digits 0-9 for 8 letters
    for perm in itertools.permutations(range(10), 8):
        # Create a dictionary mapping each letter to a digit
        letter_to_digit = dict(zip('SENDMORE', perm))
        
        # Get the values of SEND, MORE, and MONEY using the letter-to-digit mapping
        SEND = letter_to_digit['S'] * 1000 + letter_to_digit['E'] * 100 + letter_to_digit['N'] * 10 + letter_to_digit['D']
        MORE = letter_to_digit['M'] * 1000 + letter_to_digit['O'] * 100 + letter_to_digit['R'] * 10 + letter_to_digit['E']
        MONEY = letter_to_digit['M'] * 10000 + letter_to_digit['O'] * 1000 + letter_to_digit['N'] * 100 + letter_to_digit['E'] * 10 + letter_to_digit['Y']
        
        # Check if the equation SEND + MORE = MONEY holds
        if SEND + MORE == MONEY:
            # If the equation is valid, print the result
            print(f"SEND: {SEND}, MORE: {MORE}, MONEY: {MONEY}")
            print(f"Letter to Digit Mapping: {letter_to_digit}")
            return

    print("No solution found")

# Run the cryptarithmetic solver
cryptarithmetic()
