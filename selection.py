def sumOfList(arr):

    s = 0

    for i in range(0,len(arr)):
        s = s + arr[i]


    return s

l = [12,21,65,6953,325,65,123,54,12,514,545,4,5454]
print(sumOfList(l))



def sumOfMatrix(arr):

    s = 0

    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            s = s + arr[i][j]

    return s
l = [[2,1],
     [3,1,212,212,1231,12]]

print(sumOfMatrix(l))
