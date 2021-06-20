graph = [[1,9],
         [0,8],
         [3],
         [2,4,5],
         [3],
         [3,6],
         [5,7],
         [3,6,8,10,11],
         [1,7,9],
         [0,8],
         [7,11],
         [7,10],
         []]

prev  = [-1]*13

def shortestPath(graph,u,v):
    q = []
    q.append(u)
    n = len(graph)
    visited = [False]*n
    visited[u] = True

    

    while len(q)!=0:
        node = q.pop(0)

        for i in range(len(graph[node])):

            neighbor = graph[node][i]
            
            if visited[neighbor] == False:
                q.append(neighbor)
                prev[neighbor] = node

                visited[neighbor] = True

    path = []

    i = v
    while i != -1:
        path.append(i)
        i = prev[i]

    path.reverse()
    print(path)


shortestPath(graph,0,6)

