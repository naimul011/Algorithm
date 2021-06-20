graph = [[(1,4),(2,1)],
         [(3,1)],
         [(1,2),(3,5)],
         [(4,3)],
         []]


for i in range(len(graph)):
    for neigbour,weight in graph[i]:
        print(i,"-->",neigbour," cost ",weight)
