import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1000,700)
screen.tracer(0,0)
screen.title('Quick Sort Animation - PythonTurtle.Academy')
turtle.speed(0)
turtle.hideturtle()

def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

def draw_bars(v,n,currenti=-1,currentj=-1):
    turtle.clear()
    x = -400
    w = 800/n
    for  i in range(n):
        if i == currenti: turtle.fillcolor('red')
        elif i == currentj: turtle.fillcolor('blue')
        else: turtle.fillcolor('gray')
        draw_bar(x,-200,w,v[i]/2)
        x += w
    screen.update()

def partition(v,x,y):
    p = random.randint(x,y)
    v[p], v[y] = v[y], v[p]
    pivot = v[y]
    i, j = x, y-1
    while i <= j:
        while v[i] <= pivot and i <= j:
            draw_bars(v,n,i,j)
            i += 1
        while v[j] > pivot and j >= i:
            draw_bars(v,n,i,j)
            j -= 1
        if i < j:
            draw_bars(v,n,i,j)
            v[i], v[j] = v[j], v[i]
    v[i], v[y] = v[y], v[i]
     
    return i
def mergeSort(alist):

   print("Splitting ",alist)
   
   if len(alist)>1:
       mid = len(alist)//2
       l = alist[:mid]
       r = alist[mid:]

       #recursion
       mergeSort(l)
       mergeSort(r)

       i=0
       j=0
       k=0

       while i < len(l) and j < len(r):
           if l[i] < r[j]:
               alist[k]=l[i]
               draw_bars(v,len(v),i,k)
               i=i+1
           else:
               alist[k]=r[j]
               draw_bars(v,len(v),j,k)
               j=j+1
           k=k+1

       while i < len(l):
           alist[k]=l[i]
           i=i+1
           k=k+1
           draw_bars(v,len(v),i,j)

       while j < len(r):
           alist[k]=r[j]
           j=j+1
           k=k+1
           draw_bars(v,len(v),i,j)
   print("Merging ",alist)
   
def quick_sort(v,x,y):
    if x >= y:
        return
    m = partition(v,x,y)
    quick_sort(v,x,m-1)
    quick_sort(v,m+1,y)

def insertionSort(arr):

    for i in range(1,len(arr)):

        if arr[i] < arr[i-1]:
            
            toInsert = arr[i]
            j = i 

            
            while True:
                arr[j] = arr[j-1]
                j = j - 1
                draw_bars(v,n,i,j)
                if toInsert >= arr[j-1] or j<=0:
                    break

            arr[j] = toInsert
    
n = 50
v = [0] * n
for i in range(n):
    v[i] = random.randint(1,800)

t1 = time.time()
#quick_sort(v,0,n-1)
#insertionSort(v)
mergeSort(v)
turtle.clear()
draw_bars(v,n,-1)
turtle.update()
t2 = time.time()
print('elapsed time=', t2-t1)
