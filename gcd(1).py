def gcd(x,y):

    r = x%y
    while r!=0 :
        x = y
        y = r
        r = x%y

    return y

a = int(input())
b = int(input())
print('The GCD of ',a,' and ',b,' is ',gcd(a,b))
        
