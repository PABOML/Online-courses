# Uses python3
import sys
import numpy as np
import math

def optimal_weight(W, w):
#...................Pauls code......................
    w=sorted(w)
    
    a= np.ones((len(w)+1, W + 1))*math.inf # establish matrix
    a[0,:] = 0
    a[:,0] = 0
    j_add=0
    i_add=0

    for i in range (1,len(w)+1): 
        for j in range (1, W+1):
            if w[i-1] <= j: 
                a[i,j] = max(w[i-1] + a[i-1,j - w[i-1]], a[i-1,j])
            else:
                a[i,j] = a[i-1,j]
    return int( a[len(w),W] )

#...................................................
    
'''
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
'''

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
