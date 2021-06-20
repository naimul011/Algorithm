Hanoi(n,A,B,C):
    if n>0:
        Hanoi(n-1,A,B,C)
        print('Move from ',A,' -> ',B)
        Hanoi(n-1,B,C,A)


Hanoi(3,'A','B','C')
