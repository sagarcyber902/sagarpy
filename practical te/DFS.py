def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # Push adjacent vertices onto the stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}    0
start_vertex = 'A'

print("Depth-First Search (DFS) starting from vertex", start_vertex)
dfs(graph, start_vertex)
DFS
p
