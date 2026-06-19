from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(1)