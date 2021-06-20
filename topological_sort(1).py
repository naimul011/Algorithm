graph = [[1,3],
         [2,3],
         [5,6],
         [4],
         [5],
         [6],
         []]



def dfs(i,visitedNodes,visited,graph):
    visited[i] = True

    for j in graph[i]:
        if visited[j] == False:
            dfs(j,visitedNodes,visited,graph)

    visitedNodes.append(i)
    
def topSort(graph):
    n =  len(graph)
    visited = [False]*n
    ordering = []

    for i in range(n):
        if visited[i] == False:
            visitedNodes = []
            dfs(i,visitedNodes,visited,graph)

            for node in visitedNodes:
                ordering.append(node)
                
    ordering.reverse()
    return ordering

print(topSort(graph))
    
