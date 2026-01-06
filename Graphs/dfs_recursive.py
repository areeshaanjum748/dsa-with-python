def dfs(graph, source):
    visited = set()
    result = []
    
    def dfs_helper(graph, current):
        visited.add(current)
        result.append(current)
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                dfs_helper(graph, neighbour)
                
    dfs_helper(graph, source)
    
    return result
    
graph = {
    0 : [1, 2],
    1 : [3],
    2 : [],
    3 : []
}

print(dfs(graph, 0))

        

