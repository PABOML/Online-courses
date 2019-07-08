# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


#...........Pauls code...............

'''
# Inconvenient code from last assignment parts

def fibonacci_partial_sum(from_, to):
    pisano_period = 60    # pisano period of 10 (because of % 10) is 60
   # remainder_from_=from_ % pisano_period
   # remainder_to=to % pisano_period
    F=list(range(0, to + 3))
    
    if (to <= 1):
        F[to]=to
        return (F[to + 1] - 1) % 10  # HINT: sum(F(n))= F(n+2)-1 
    
    else:
        for i in range(2, to + 3):
            F[i]=(F[i-1] % 10 + F[i-2] % 10) % 10

        return (( F[to + 2] - 1 ) - ( F[from_ + 1] - 1) ) % 10  # HINT: sum(F(n))= F(n+2)-1 
'''
    
def fibonacci_partial_sum(from_, to):
    return  (fibonacci_sum(to) - fibonacci_sum(from_ - 1)) % 10
    
def fibonacci_sum(n):
    return (get_fibonacci(n+2) - 1 )  % 10
            
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
    a=random.randint(0,1000)
    b=random.randint(1,1000)
    to = min(a,b)
    from_=max(a,b)
    
    print(to, from_)
    x=fibonacci_partial_sum_naive(to, from_)
    y=fibonacci_partial_sum(to, from_)
        
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
  # from_, to=[int(x) for x in input().split()]
   from_, to = map(int, input().split())
   #print(fibonacci_partial_sum(from_, to)) 
   print(fibonacci_partial_sum(from_, to)) 