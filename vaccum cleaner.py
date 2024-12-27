class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Start position at (0, 0)
        
    def move_left(self):
        if self.position[1] > 0:  # Ensure within bounds
            self.position = (self.position[0], self.position[1] - 1)
    
    def move_right(self):
        if self.position[1] < len(self.environment[0]) - 1:  # Ensure within bounds
            self.position = (self.position[0], self.position[1] + 1)
    
    def move_up(self):
        if self.position[0] > 0:  # Ensure within bounds
            self.position = (self.position[0] - 1, self.position[1])
    
    def move_down(self):
        if self.position[0] < len(self.environment) - 1:  # Ensure within bounds
            self.position = (self.position[0] + 1, self.position[1])
    
    def clean(self):
        x, y = self.position
        if self.environment[x][y] == "D":  # D = dirty
            self.environment[x][y] = "C"  # C = clean
            print(f"Cleaned position {self.position}")
    
    def is_clean(self):
        x, y = self.position
        return self.environment[x][y] == "C"
    
    def run(self):
        while not self.is_done():
            print(f"Current position: {self.position}, Environment: {self.environment}")
            if not self.is_clean():
                self.clean()
            self.move_to_next_position()

    def move_to_next_position(self):
        # For simplicity, move right, then down, and then left when reaching the end
        if self.position[1] < len(self.environment[0]) - 1:  # Move right
            self.move_right()
        elif self.position[0] < len(self.environment) - 1:  # Move down
            self.move_down()
        elif self.position[1] > 0:  # Move left
            self.move_left()
        else:
            print("Grid cleaned!")
            return

    def is_done(self):
        # If all cells are clean, return True
        for row in self.environment:
            if "D" in row:
                return False
        return True

# Define a simple 2x2 grid environment
# "D" = Dirty, "C" = Clean
environment = [
    ["D", "D"],
    ["D", "C"]
]

# Initialize the vacuum cleaner
vacuum = VacuumCleaner(environment)

# Run the vacuum cleaner agent
vacuum.run()

