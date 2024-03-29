# python3

import sys

n, m = map(int, sys.stdin.readline().split())
#n, m = map(int, input().split())

lines = list(map(int, sys.stdin.readline().split()))
#lines = list(map(int, input().split()))

rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    
    if table !=parent[table]:
        parent[table] = getParent(parent[table])
        
    return parent[table]

def merge(destination, source, ans):
    realDestination, realSource = getParent(destination), getParent(source) 

    if realDestination == realSource:
        return ans
    
    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination], lines[realSource] = lines[realDestination] + lines[realSource], 0
        if lines[realDestination] > ans:
            ans = lines[realDestination]
        return ans
            
    else:
        parent[realDestination] = realSource
        lines[realSource], lines[realDestination] = lines[realDestination] + lines[realSource], 0
        if lines[realSource] > ans:
            ans = lines[realSource]
            
        if rank[realDestination] == rank[realSource]:
            rank[realSource] = rank[realSource] + 1
        return ans
            
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    #destination, source = map(int, input().split())
    ans = merge(destination - 1, source - 1, ans)
    print(ans)
    
