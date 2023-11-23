from load import load_numbers
import sys

# Finds the index of the smallest number value
def smallest_value_index(list):
    index = 0
    
    for i in range(len(list)):
        if list[i] < list[index]:
            index = i

    return index

# Selection for algorithm
# Finds the smallest value in the list argument, adds it to the sorted list
# Loops until no elements are left in the array
def selection_sort(list):
    sorted_list = []

    for i in range(len(list) ):
        smallest = smallest_value_index(list)
        sorted_list.append(list.pop(smallest))

    return sorted_list

numbers = load_numbers(sys.argv[1])

print(selection_sort(numbers))