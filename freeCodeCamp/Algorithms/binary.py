def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        # // is floor division, rounds number to nearest integer
        middle = (first + last) // 2

        if list[middle] == target:
            return middle
        elif list[middle] < target:
            # +1 because we dont need to include the middle point as the value is bigger
            first = middle + 1
        else:
            # -1 because we dont want to include the middle point as the value is smaller
            last = middle - 1


arr = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(arr, 123))