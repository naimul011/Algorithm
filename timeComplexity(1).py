import time
import math


def isPrime1(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False

    return True


def isPrime2(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False

    return True

#Algorithm 1
start = time.time()
print(isPrime1(1051601))
timeTaken =  time.time() - start

print(timeTaken*1000)

#Algorithm 2
start = time.time()
print(isPrime2(1051601))
timeTaken =  time.time() - start

print(timeTaken*1000)
