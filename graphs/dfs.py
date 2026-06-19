graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

def dfs(node,visited):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)
dfs(1,set())