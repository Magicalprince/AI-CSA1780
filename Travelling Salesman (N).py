from itertools import permutations

def traveling_salesman_problem(graph, start):
    """Solve the Traveling Salesman Problem (TSP) using brute force."""
    # Get all the cities excluding the starting city
    cities = list(graph.keys())
    cities.remove(start)
    
    # Generate all permutations of the cities
    all_routes = permutations(cities)
    min_distance = float('inf')  # Initialize minimum distance as infinity
    best_route = None
    
    # Calculate the total distance for each route
    for route in all_routes:
        # Start the route with the starting city
        total_distance = 0
        current_city = start
        
        # Calculate distance for the current route
        for next_city in route:
            total_distance += graph[current_city][next_city]
            current_city = next_city
        
        # Return to the starting city
        total_distance += graph[current_city][start]
        
        # Update the shortest route
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route
    
    # Print the result
    print(f"Minimum distance: {min_distance}")
    print(f"Best route: {start} -> {' -> '.join(best_route)} -> {start}")

# Example usage
if __name__ == "__main__":
    # Define the graph as a dictionary of dictionaries
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    
    # Starting city
    start_city = 'A'
    
    print(f"Traveling Salesman Problem starting from {start_city}:")
    traveling_salesman_problem(graph, start_city)
