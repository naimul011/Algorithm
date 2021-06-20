n = 13
cc = 0

#graph = [[1,9],
#         [0,8],
#         [3],
#         [2,4,5],
#         [3],
#         [3,6],
#         [5,7],
#         [3,6,8,10,11],
#         [1,7,9],
 #        [0,8],
#         [7,11],
 #        [7,10],
#         []]

graph = [[2, 3],
         [],
         [0],
         [0, 4],
         [3],
         [6, 7],
         [5],
         [5],
         []]
    
visited = [False]*n

def dfs(i):
    if visited[i]:
        return

    #print('Visiting node ',i)
    visited[i] = True

    for j in graph[i]:
        dfs(j)

    #print('Backtracking node ',i)

for u in range (len(graph)):
    if visited[u] == False:
        cc+=1
        dfs(u)
print(cc)
