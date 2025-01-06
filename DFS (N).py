def dfs(graph, start, visited=None):
    """Perform Depth First Search (DFS) on a graph."""
    if visited is None:
        visited = set()  # Initialize the visited set if not already done

    # Mark the current node as visited
    visited.add(start)
    print(start, end=" ")  # Print the node as we visit it

    # Recur for all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == "__main__":
    # Define a simple graph using an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("DFS starting from node A:")
    dfs(graph, 'A')
