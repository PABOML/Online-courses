# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

#.........Pauls code..............    
def get_fibonacci_huge(n, m):
    pisano_period = get_pisano_period(m)
    remainder=n % pisano_period
    return calc_fib_fast(remainder) % m

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
        
def calc_fib_fast(n):
    F=list(range(0,n+1))
    if (n <= 1):
        return n
    
    else:
        for i in range(2,n+1):
            F[i]=F[i-1]+F[i-2]
        return F[n]
#.................................


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
   # print(get_fibonacci_huge(n, m))
    print(get_fibonacci_huge(n, m))