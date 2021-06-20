graph = [[1,2],
         [2,3],
         [5,6],
         [4],
         [5],
         [6],
         []]

    
def topSort(graph):
    n = len(graph)
    visited = [False]*n
    ordering = []
    j = n - 1
    
    for i in range(n):
        if visited[i] == False:
            visitedNodes = []
            dfs(i,visitedNodes,visited,graph)

            for node in visitedNodes:
                ordering.append(node)
                
    ordering.reverse()
    return ordering

def dfs(i,visitedNodes,visited,graph):
    visited[i] = True

    for j in graph[i]:
        if visited[j] == False:
            dfs(j,visitedNodes,visited,graph)
    visitedNodes.append(i)




print(topSort(graph))
