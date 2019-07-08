# python3
import sys



#.....................Paul.................................
def compute_min_refills(distance, tank, stops):
    n=len(stops)
    x=[0]+stops+[d]

    numRefills=0
    currentRefill=0
    while currentRefill <= n:
        lastRefill = currentRefill
    
#...... Inner loop maximizes drive to next station (safe greedy move)......    
        while currentRefill <= n and (x[currentRefill + 1] - x[lastRefill]) <= m:
            currentRefill = currentRefill + 1
#..........................................................................   
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills = numRefills + 1
 
    return numRefills
    
#.......................................................... 

#return -1

if __name__ == '__main__':
    #d, m, _,*stops = list(map(int, input().strip().split()))
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
