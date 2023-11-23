from load import load_numbers
import sys

# Takes the first value from the list
# Makes two list:
# 1. with values less or equal to the first value of the list(pivot) without the said value(starts from 1)
# 2. with values that are more than the first value of the list(pivot)
# Why it works:
# Because it keeps on adding values to smaller and bigger lists until there are only 1 element each left
# Then it merges them, because they are sorted
# If more list or less list is None, when added together we get none, and the function returns
# NOTE: may cause errors with repeated values
def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    less = []
    more = []

    for value in list[1:]:
        if value > pivot:
            more.append(value)
        else:
            less.append(value)
    
    # Sorts less list in the same way
    # Adds the pivot value to it(>= to the returned last element)
    # Sorts more list also in the same way
    # Adds the more sorted list
    # Returns everything
    return quick_sort(less) + [pivot] + quick_sort(more)

numbers = load_numbers(sys.argv[1])

print(quick_sort(numbers))