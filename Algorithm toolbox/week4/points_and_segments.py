# Uses python3
import sys, random, math, operator
sys.setrecursionlimit(150000) 
#.....................Pauls mergesort algorithm.......................
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions 
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge_and_count(a, b, left, right, ave)
    return b
    return number_of_inversions 
#...............Pauls code....................
def merge_and_count(a, b, left, right, ave):
    i,j=left,ave
    k=left
    inv=0
    while i < ave and j < right:            
        if a[i] <= a[j]:
            b[k]=a[i]
            i+=1
        else:
            b[k]=a[j]
            j+=1
            inv+=len(a[i:ave])
        k+=1
            
    while i < ave:
        b[k]= a[i]
        i+=1
        k+=1
                 
    while j < right:
        b[k]=a[j]
        j+=1
        k+=1
    for i in range(left, right):
        a[i]=b[i]         
    return inv

#.....................................................................

#................Pauls quick sort code................................

def partition3(a, l, r):

    x = a[l]
    j = l;
    y= 0# counter of equals a[i] = x
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j+y] = a[j+y], a[i]
            a[j+y], a[j] = a[j], a[j+y]
            
        elif a[i] == x:
            y += 1
            a[i], a[j+y] = a[j+y], a[i]
            #a[j+y], a[j] = a[j], a[j+y]
                
    a[l], a[j] = a[j], a[l]
    return j,y
    
def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k =random.randint(l, r)
    #print(k)
    a[l], a[k] = a[k], a[l] # Swapping of leftmost a[l] and with random item in list a [k]
    #use partition3
    m,y = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + y + 1, r);
    return a
    
#....................Pauls binary search code...............................
def binary_search_starts(a, x): # starts/ends, points
    left, right = 0, len(a)
    l=0
    while right >= left and left+1 <= len(a):
        mid = math.floor(left + (right-left)/2)
        if x < a[mid]:
            right = mid-1
        elif x >= a[mid]:
            l+=len(a[left:mid+1])
            left = mid+1
    return l

def binary_search_ends(a, x): # starts/ends, points
    left, right = 0, len(a)
    r=0
    while right >= left and left+1 <= len(a):
        mid = math.floor(left + (right-left)/2)
        if x <= a[mid]:
            r+=len(a[mid:right+1])
            right = mid-1
        elif x > a[mid]: 
            left = mid+1
    return r

#.......................Pauls code..................................
def fast_count_segments_1(starts, ends, points):
    cnt = [0] * len(points)
    starts, ends= sorted(starts), sorted(ends)
    for i in range(0,len(points)):
        l,r=binary_search_starts(starts,points[i]), binary_search_ends(ends,points[i])

        cnt[i]=l+r-len(starts) # Mengenlehre: Full set n = segment starts left or =point + segment ends right or =point - no of segments
    return cnt
#...................................................................
# alternative fast_count algorithm suggested by Alexander Kulikov in the forum

def fast_count_segments(starts, ends, points):
    b=[]
    for i in range(0, len(starts)):
        b.append((starts[i], 'l'))
    for i in range(0, len(ends)):
        b.append((ends[i], 'r'))
    for i in range(0, len(points)):
        b.append((points[i], 'p',i))
    
    a = sorted(b, key = operator.itemgetter(0,1))
    cnt=[0]* len(points)
    l,r=0,0
    
    for tups in a:
        if 'l' in tups:
            l+=1
        elif 'r' in tups:
            r+=1
        else:
            cnt[tups[2]]=l-r
    return cnt
    
#...................................................................

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    #l=binary_search_starts(starts, points[0])
    #print(l)
    #starts=randomized_quick_sort(starts,0,len(starts)-1)
    #print(starts)
    for x in cnt:
        print(x, end=' ')
