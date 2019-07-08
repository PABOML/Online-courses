# Uses python3
import sys
import numpy as np

#.................Pauls code............

value=0.

#initial_vw_ratio=[0.] * n
#for i in range(0, n-1):
#intial_vw_ratio = values[i] / weights [i]
 
'''
def get_optimal_value(capacity, weights, values):
    value=0.
    
    if capacity == 0 or n == 0:
        return 0
    
    while capacity > 0:
    #for i in range(n):
        index=sorted_index(weights, values)
        if weights[index] !=0:
            take_weight=min(capacity, weights[index])
            value = value + take_weight * (values[index] / weights[index])
            capacity=capacity - take_weight
            weights[index]=weights[index] - take_weight
     
    return value

def sorted_index(weights, values):
    index=-1
    max_vw_ratio= 0
    for i in range(0, n):
        if weights[i] != 0 and (values[i] / weights[i]) > max_vw_ratio:
            max_vw_ratio = values[i] / weights [i]
            index= i
    return index
'''

def get_optimal_value(capacity, weights, values):
    value = 0.
    if capacity == 0:
        return 0
    for i in range(n):
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            available_weights = min(capacity, weights[max_index])
            value = value + available_weights * values[max_index]/weights[max_index]
            weights[max_index] = weights[max_index] - available_weights
            capacity = capacity - available_weights

    return value

def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(n):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i]/weights[i]
            index = i
    return index
#.......................................


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().strip().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    #print(opt_value)
