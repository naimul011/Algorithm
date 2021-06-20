import random

def insertionSort(arr):

    for i in range(1,len(arr)):

        if arr[i] < arr[i - 1]:

            toInsert = arr[i]
            j = i

            while True:

                arr[j] = arr[j-1]
                j = j - 1

                if toInsert >= arr[j-1] or j <= 0:
                    break

            arr[j] = toInsert




l = random.sample(range(1, 50), 10)
print('Unsorted ',l)

insertionSort(l)
print('Sorted ',l)

