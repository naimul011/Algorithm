graph = [[(1,4),(2,1)],
         [(3,1)],
         [(1,2),(3,5)],
         [(4,3)],
         []]


for i in range(len(graph)):
    for neigbour,weight in graph[i]:
        print(i,"-->",neigbour," cost ",weight)


pq = []

pq.append((1,'A'))
pq.append((0,'Z'))
pq.append((4,'M'))
pq.append((2,'A'))
pq.append((3,'Z'))
pq.append((1,'M'))


pq.sort(reverse=True)
print(pq.pop())
