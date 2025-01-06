from collections import deque

def bfs(graph, start):
    visited = set()  # Keeps track of visited nodes
    queue = deque([start])  # Queue to manage the BFS process
    result = []  # To store the order of nodes visited

    while queue:
        node = queue.popleft()  # Get the first node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)  # Add it to the result
            for neighbor in graph[node]:  # Iterate through its neighbors
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue

    return result  # Return the order of visited nodes

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS starting from node 'A'
print("BFS Traversal:", bfs(graph, 'A'))
