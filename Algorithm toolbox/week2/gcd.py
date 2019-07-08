# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


#......Pauls code........

def gcd(a, b):    
    current_gcd=1
    residual=max(a, b) % min(a, b)
    while residual !=0:
        a = min(a,b)
        b = residual
        residual=max(a,b) % min(a,b)
        
    else: 
        current_gcd = min(a,b)
    
    return current_gcd

#........................
'''
#.... Stress test....
while True:
    import random
    a=random.randint(1,1000000)
    b=random.randint(1,1000000)
    
    print(a, b)      
    x=gcd_naive(a, b)
    y=gcd(a, b)
        
    if x==y:
        print (x)
        print (y)
        print ('OK')

    else:
        print (x)
        print (y)
        print ('Wrong answer')
        break
'''




if __name__ == "__main__":
    
    a, b = [int(x) for x in input().split()]
    #input = sys.stdin.read()
   # input = int(input())
    #a, b = map(int, input.split())
    print(gcd(a, b))