# Function to perform graph coloring
def graph_coloring(graph):
    # Number of vertices
    n = len(graph)
    
    # Result array to store assigned colors (initially all uncolored)
    result = [-1] * n
    
    # Assign the first color to the first vertex
    result[0] = 0
    
    # Temporary array to check availability of colors
    available_colors = [False] * n
    
    # Assign colors to remaining vertices
    for u in range(1, n):
        # Mark colors used by adjacent vertices as unavailable
        for v in range(n):
            if graph[u][v] == 1 and result[v] != -1:  # Adjacent and already colored
                available_colors[result[v]] = True

        # Find the first available color
        color = 0
        while color < n and available_colors[color]:
            color += 1
        
        # Assign the found color to the vertex
        result[u] = color

        # Reset the availability array for the next iteration
        available_colors = [False] * n
    
    # Print the result
    print("Vertex Colors:")
    for vertex in range(n):
        print(f"Vertex {vertex}: Color {result[vertex]}")

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Call the function
graph_coloring(graph)
