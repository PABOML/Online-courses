# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


#......Pauls code.......

def lcm(a, b):    
    initial_ab=a*b
    current_gcd=1
    residual=max(a, b) % min(a, b)
    while residual !=0:
        a = min(a,b)
        b = residual
        residual=max(a,b) % min(a,b)
        
    else: 
        current_gcd = min(a,b)
    
    return int(initial_ab//current_gcd)

#........................
'''
def lcm(a,b):
    for l in range(1, b):
        if (l*a) % b == 0:
            return l*a
    
    return a*b
'''        
'''        
#.... Stress test....
while True:
    import random
    a=random.randint(1,10)
    b=random.randint(1,10)
    
    print(a, b)      
    x=lcm_naive(a, b)
    y=lcm(a, b)
        
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

#.......................

if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    
    #    input = sys.stdin.read()
 #   a, b = map(int, input.split())
    print(lcm(a, b))

