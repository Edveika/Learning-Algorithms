import random
import sys
from load import load_numbers

def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    
    return True

def bogo_sort(list):
    count = 0
    while not is_sorted(list):
        random.shuffle(list)
        count += 1
    
    print(count)

    return list

numbers = load_numbers(sys.argv[1])

print(bogo_sort(numbers))