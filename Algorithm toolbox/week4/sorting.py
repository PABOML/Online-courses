# Uses python3
import sys
import random
sys.setrecursionlimit(150000) 

def partition3(a, l, r):
#................Pauls code..............
    x = a[l]
    j = l;
    y= 0 # counter of equals a[i] = x
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j+y] = a[j+y], a[i]
            a[j+y], a[j] = a[j], a[j+y]
            
        elif a[i] == x:
            y += 1
            a[i], a[j+y] = a[j+y], a[i]
                
    a[l], a[j] = a[j], a[l]
    return j,y


#........................................  
    #pass

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


    
def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k =random.randint(l, r)
    a[l], a[k] = a[k], a[l] # Swapping of leftmost a[l] and with random item in list a [k]
    #use partition3
    m,y = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + y + 1, r);
    
#.... Stress test....
'''
import random
def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res

while True:    
    n=random.randint(5)
    a_2=Rand(0,9000000,n)
    a_3=a_2
    print(a_2)      
    x,y=randomized_quick_sort_2(a_2, 0, n - 1), randomized_quick_sort_3(a_3, 0, n - 1)
        
    if x==y:
        print (a_2)
        print (a_3)
        print ('OK')

    else:
        print (a_2)
        print (a_3)
        print ('Wrong answer')
        break

    
    
    
'''  
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')