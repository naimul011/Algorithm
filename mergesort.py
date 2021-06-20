def split(alist):
	mid = len(alist)//2
	return alist[:mid], alist[mid:]

def merge(alist,l,r):
    i,j,k = 0,0,0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            alist[k] = l[i]
            i += 1
        else:
            alist[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        alist[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        alist[k] = r[j]
        j += 1
        k += 1

def mergeSort(alist):
    if len(alist) > 1:
        l , r = split(alist)
        print(l,' ',r)
        mergeSort(l)
        mergeSort(r)

        merge(alist,l,r)
        print(alist)

alist = [8, 3, 5, 1, 4, 6, 9, 2]
mergeSort(alist)
print(alist)
