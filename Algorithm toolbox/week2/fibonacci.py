# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
        
    return calc_fib(n - 1) + calc_fib(n - 2)

# Pauls code
#........................
def calc_fib_fast(n):
    F=list(range(0,n+1))
    if (n <= 1):
        return n
    
    else:
        for i in range(2,n+1):
            F[i]=(F[i-1]+F[i-2]) % 10
        return F[n]
       

'''
     n= 0 1 2 3 4 5 6  7  8  9
Fib(n)= 0 1 1 2 3 5 8 13 21  34
'''
'''
#.... Stress test....
while True:
    import random
    n=random.randint(1,30)
    
    print(n)      
    x=calc_fib_fast(n)
    y=calc_fib(n)
        
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

#........................
n = int(input())
print(calc_fib_fast(n))
