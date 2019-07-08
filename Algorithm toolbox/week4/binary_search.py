# Uses python3
import sys, math

def binary_search(a, x):
    left, right = 0, len(a)
#...............Pauls code.....................
    while right >= left and left+1 <= len(a):
        mid = math.floor(left + (right-left)/2)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1

'''    Recursive calls 
    if right <= left:
        return -1
    mid = math.floor(left + (right-left)/2)
    
    if x == a[mid]:
        return mid
    
    elif x < a[mid]:
        return binary_search(a[left:mid], x) #a[left:mid]
        
    else:
        return binary_search(a[mid+1:right+1], x) -> problems with finding the mid of the initial array a
        
        '''
#..............................................
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    input = int(input())
    data = list(map(int, input.split()))
    #data=list(data)

    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
