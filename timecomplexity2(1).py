import math
import time

def is_prime1(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True

def is_prime2(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False

    return True

start = time.time()
print(is_prime1(1051601))
print(time.time()-start)

start = time.time()
print(is_prime2(1051601))
print(time.time()-start)

