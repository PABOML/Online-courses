# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


#...........Pauls code...............

# Hint: F(0)^2 + F(1)^2 +...+ F(n)^2 = F(n+1) * F(n)



def fibonacci_sum_squares(n):
    if n % 60 == 0 or n % 60 == 59:
        return 0
    else:
        return ( (get_fibonacci(n) % 10) * (get_fibonacci(n+1)) % 10 ) % 10
            
def get_fibonacci(n):
    
    pisano_period = 60    # pisano period of 10 (because of % 10) is 60
    remainder=n % pisano_period
    
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    next_ = current + previous
    
    for _ in range (remainder-1):
        next_= (current + previous) % 10
        previous = current % 10
        current = next_
        
    return next_


'''
#.... Stress test....
while True:
    import random
    n=random.randint(0,1000)
   # b=random.randint(0,1000)
   # to = min(a,b)
   # from_=max(a,b)
    
    print(n)
    x=fibonacci_sum_squares_naive(n)
    y=fibonacci_sum_squares(n)
        
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
#....................................

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
