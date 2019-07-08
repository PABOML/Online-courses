# Uses python3
import sys, math

def get_majority_element(a, left, right):
    # Base case 1: Array a is empty
    if left == right:
        return -1
    # Base case 2: Array a has 1 element
    if left + 1 == right:
        return a[left]
#..............Pauls code...................
    #while left < right and left <= len(a):
    else:
        mid = math.floor(left + (right-left)/2)
        
        a_left=get_majority_element(a, left, mid)
        a_right=get_majority_element(a, mid, right)
        
    if a[left:right].count(a_left) > len(a[left:right])/2: 
        return a_left
    elif a[left:right].count(a_right) > len(a[left:right])/2 :
        return a_right
    else:
        return -1
#...........................................

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
