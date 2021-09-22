def BFS(src):
    queue = [src]
    color = [None] * len(graph)
    color[src] = True
    while queue:
        src = queue.pop(0)

        for adj in graph[src]:
            if color[src] == color[adj]:
                return 'NOT BICOLORABLE.'

            if color[adj] == None:
                queue.append(adj)
                color[adj] = not color[src]
        
    return 'BICOLORABLE.'

if __name__ == '__main__':
    while int(input()):
        graph = {}

        for _ in range(int(input())):
            s, t = map(int, input().split())
            graph.setdefault(s, []).append(t)
            graph.setdefault(t, []).append(s)

        print(BFS(0))
