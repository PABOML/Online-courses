# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
#    return previous, current

    return current % 10


#.........Pauls code..........
'''
def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for _ in range(n-1):
        previous = current + current
        current =  previous + current
        
        return current 
'''
def get_fibonacci_last_digit(n):
    F=list(range(0,n+1))
    if (n <= 1):
        return n
    
    else:
        for i in range(2,n+1):
            F[i]=F[i-1] % 10 + F[i-2] % 10
        return F[n] % 10

# Fibonacci example    
# n=    0 1 2 3 4 5 6 7
# F(n)= 0 1 1 2 3 5 8 13   
    
    
#.............................

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
