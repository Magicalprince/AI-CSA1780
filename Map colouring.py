def is_safe(graph, color, v, c):
    # Check if any adjacent vertex has the same color
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def map_coloring_util(graph, m, color, v):
    # If all vertices are assigned a color then return True
    if v == len(graph):
        return True

    # Try different colors for vertex v
    for c in range(1, m+1):
        # Check if it is safe to color vertex v with color c
        if is_safe(graph, color, v, c):
            color[v] = c

            # Recur to assign colors to the rest of the vertices
            if map_coloring_util(graph, m, color, v + 1):
                return True

            # If assigning color c doesn't lead to a solution, reset the color
            color[v] = 0

    return False

def map_coloring(graph, m):
    # Initialize all vertices as uncolored (0)
    color = [-1] * len(graph)

    # Start coloring the graph from vertex 0
    if not map_coloring_util(graph, m, color, 0):
        return False

    # If coloring is successful, return the coloring
    print_solution(color)
    return True

def print_solution(color):
    print("Solution:")
    for c in color:
        print(c, end=" ")
    print()

# Example usage
if __name__ == "__main__":
    # Represent the map as a graph (adjacency matrix)
    # 0: No edge, 1: Edge (adjacent)
    # Here, we represent a map with 4 regions and 4 colors (m=4)
    graph = [
        [0, 1, 1, 0],  # Region 0 is adjacent to Region 1 and 2
        [1, 0, 1, 1],  # Region 1 is adjacent to Region 0, 2, and 3
        [1, 1, 0, 1],  # Region 2 is adjacent to Region 0, 1, and 3
        [0, 1, 1, 0]   # Region 3 is adjacent to Region 1 and 2
    ]

    # Maximum number of colors (4-color map problem)
    m = 3

    if not map_coloring(graph, m):
        print("Solution does not exist")
