# Uses python3
import sys, math
#NotebookApp.iopub_data_rate_limit=10000000.0 #(bytes/sec)
#NotebookApp.rate_limit_window=10.0 #(secs)



def optimal_sequence_greedy_n_to_1(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence_dp(n):
    #operations=[*2, *3, +1]
    sequence=[]
    if n<=1:
        sequence.append(n)
    else:
        min_comp = (n) * [math.inf]
        min_comp[0] = 0
    
        for i in range(1,n+1):
            num_comp = min_comp[i-2] + 1
            if num_comp < min_comp[i-1]:
                min_comp[i-1] = num_comp
                    
            if i % 2 == 0:
                num_comp = min_comp[(i // 2) - 1] + 1
                if num_comp < min_comp[i-1]:
                    min_comp[i-1] = num_comp
                    
            if i % 3 == 0:
                num_comp = min_comp[(i // 3) - 1] + 1
                if num_comp < min_comp[i-1]:
                    min_comp[i-1] = num_comp 
                
        sequence.append(n)         
        while n >= 2:
            
            num_comp = min_comp[n-2]
            sequence.append(n - 1)
            
            if n % 2 == 0 and min_comp[n // 2 - 1] < num_comp:
                num_comp = min_comp[n // 2 - 1]
                sequence[len(sequence) - 1] = n // 2
            
            if n % 3 == 0 and min_comp[n // 3 - 1] < num_comp:
                num_comp = min_comp[n // 3 - 1]
                sequence[len(sequence) - 1] = n // 3
            
            if sequence[len(sequence)-2] - sequence[len(sequence)-1] == 1:
                n = n - 1
               
            elif sequence[len(sequence)-2] // 2 == sequence[len(sequence)-1]:
                n = n // 2
                
            else:
                n = n // 3

    return reversed(sequence)


#input = sys.stdin.read()
n = int(input())
sequence = list(optimal_sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
