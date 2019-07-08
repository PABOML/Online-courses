# Uses python3
import sys



def optimal_summands(n):
#.............Pauls code..............    
    summands = []
    n_ini=n
    for i in range(1,n_ini):
        n=n-i
        if n < i:
            summands.append(n)
            break
        elif n==0:
            summands.append(i)
            break
        else:
            summands.append(i)
#.....................................
    return summands

if __name__ == '__main__':
    n = int(input())
    #input = sys.stdin.read()
    #n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
