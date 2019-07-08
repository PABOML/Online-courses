#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
 
#...............Pauls code...................
    a.sort(reverse=True)
    b.sort(reverse=True)
    a=np.array(a)
    b=np.array(b)
    res=a.dot(b)
#............................................    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    #data = list(map(int, input().strip().split()))
    data = list(map(int, input.split()))
   
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
