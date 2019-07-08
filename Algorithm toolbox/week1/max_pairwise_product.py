# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

#--- Programmed by Paul:
def max_pairwise_product_fast(numbers):
    max_product=0
    first=numbers.index(max(numbers))
    first_number=numbers[numbers.index(max(numbers))]
    del numbers[numbers.index(max(numbers))]
    second=numbers.index(max(numbers))
    second_number=numbers[numbers.index(max(numbers))]
    max_product=first_number * second_number
            
    return max_product
#---
"""
#--- Programmed by Paul: Stress test
while True:
    import random
    n=5
    numbers=[]
    numbers
    for i in range (0, n):
        numbers.append(random.randint(1, 10))

    print(numbers)      
    x=max_pairwise_product(numbers)
    y=max_pairwise_product_fast(numbers)
        
    if x==y:
        print (x)
        print (y)
        print ('OK')

    else:
        print (x)
        print (y)
        print ('Wrong answer')
        break
    
#---"""


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
