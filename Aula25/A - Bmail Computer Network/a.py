def bfs(graph, start, end):
    queue = [[start]]
    visited = [False] * end
    
    while queue:
        path = queue.pop(0)
        last_node_of_path = path[-1]
        
        if last_node_of_path == end:
            return path
        elif not visited[last_node_of_path - 1]:
            for adjacent in graph[last_node_of_path - 1][0]:
                new_path = path + [adjacent]
                queue.append(new_path)
            visited[last_node_of_path - 1] = True
                

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))

    graph = [ [[], False] for _ in range(n)]

    for i, pi in enumerate(p, start=2):
        graph[pi - 1][0].append(i)

    print(*bfs(graph, 1, n))
