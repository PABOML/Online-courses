# Uses python3
import sys

def get_change(m):
#.................Pauls code............
    M=m # M is remaining value
    V=[10, 5, 1]
    no_of_coins=[0, 0, 0]
    while M != 0:
        for i in range(0, len(V)):
            no_of_coins[i]=int(M/V[i])
            M = M - no_of_coins[i] * V[i]
    
    return sum(no_of_coins)
#.......................................

    return m

if __name__ == '__main__':
    m = int(input())
    #m = int(sys.stdin.read())
    print(get_change(m))
