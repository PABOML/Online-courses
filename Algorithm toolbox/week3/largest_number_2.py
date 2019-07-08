#Uses python3

import sys
import math

def largest_number(digits):
    #write your code here
    res = ""
    while len(digits) !=0:
        max_digit=str(digits[0])
        for digit in digits:
            if is_greater(digit, max_digit):
                max_digit=str(digit)
        res+=max_digit
        digits.remove(max_digit)
    return res
#    for x in a:
#        res += x
 
def is_greater(digit, max_digit):
    return str(digit) + max_digit > max_digit + str(digit)

if __name__ == '__main__':
    #data = int(input().split)
    #data = list(map(int, input().strip().split()))
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
    
