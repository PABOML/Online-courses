# Uses python3
import numpy as np
import math

def edit_distance(s, t):
  
#..........................Pauls code................
    a= np.ones( (len (s) + 1, len(t) + 1)) * math.inf # establish matrix
    a[0,:] = 0
    a[:,0] = 0
    j_add=0
    i_add=0

    for i in range (0,len(s) + 1 ): # initializing matrix with 0,1,2,3....x/y
        for j in range (0, len(t) + 1):
            if i == 0:
                a[i][j]=j_add
                j_add +=1
            if j == 0:
                a[i][j]=i_add
                i_add+=1
                
    for i in range (1,len(s) + 1 ): 
        for j in range (1, len(t) + 1):
            if s[i-1] == t[j-1]:
                a[i,j] = a[i-1,j-1]
            else:
                a[i,j] = min (a[i, j - 1], a[i-1,j-1], a[i-1,j]) + 1




#....................................................
    return int(a[len (s),len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
