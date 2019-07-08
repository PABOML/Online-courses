# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

#...........Pauls code...............
     
def fibonacci_sum(n):
    pisano_period = 60
    remainder=n % pisano_period
    F=list(range(0, remainder + 1))
    
    if (n <= 1):
        n
    
    else:
        for i in range(2,remainder+1):
            F[i]=(F[i-1] % 10 + F[i-2] % 10) % 10

    
    return sum(F) % 10

    

# pisano period of 10 (because of % 10) is 60
'''
def get_pisano_period(m):
    a=0 
    b=1
    c=a+b
    for i in range(1,m*m):
        c = (a+b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i
'''
#....................................
    
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
