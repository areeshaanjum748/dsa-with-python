from collections import deque

def bfs(graph, source):
    
    result = []
    queue = deque([source])
    visited = set()
    
    visited.add(source)
    
    while queue:
        
        current = queue.popleft()
        result.append(current)
        
        for neighbour in graph[current]:
            if neighbour not in visited:
              queue.append(neighbour)
              visited.add(neighbour)
              
    return result
        
graph = {
    0 : [1, 2],
    1 : [3],
    2 : [],
    3 : []
}

print(bfs(graph, 0))
