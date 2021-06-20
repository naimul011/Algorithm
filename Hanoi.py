def Hanoi(n,A,C,B):
    if n>0:
        Hanoi(n-1,A,B,C)
        print('Move from ',A,' -> ',B)
        Hanoi(n-1,B,C,A)


Hanoi(2,'A','B','C')
