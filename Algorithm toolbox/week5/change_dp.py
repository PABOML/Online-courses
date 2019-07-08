# Uses python3
import sys, math

def get_change(m):
#.......................Pauls code...........................
    coins=[1,3,4]
    min_coins = (m+1) * [math.inf]
    min_coins[0] = 0
    
    for i in range(1,m+1):
        min_coins[i] = math.inf
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_coins[i - coins[j]] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[m]
        
    



#............................................................
   # return m // 4

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
