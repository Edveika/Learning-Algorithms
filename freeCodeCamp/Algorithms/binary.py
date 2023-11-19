def binary_search(list, target):
    # Index of the first element
    first = 0
    # Index of the last element
    last = len(list) - 1

    # Algorithm will run until first element is less or equal to last element
    while first <= last:
        # // is floor division, rounds number to nearest integer
        # Calculates the middle point of the list
        middle = (first + last) // 2

        if list[middle] == target:
            return middle
        elif list[middle] < target:
            # +1 because we dont need to include the middle point as the value is bigger
            first = middle + 1
        else:
            # -1 because we dont want to include the middle point as the value is smaller
            last = middle - 1
   
    return None


arr = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(arr, 123))