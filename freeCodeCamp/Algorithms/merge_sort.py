# Splits a list into two
def split(list):
    mid = len(list) // 2

    left = list[:mid]
    right = list[mid:]

    return left, right

# Merges left and right lists together
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are still some elements left in the left half, add them to the list
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Same to the right half
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Divide: divide list into multiple lists until each list contains 1 elements
# Conquer: sort everything in ascending order
# Combine: combine all lists into one
# Divide, conquer and combine
def merge_sort(list):
    if len(list) <= 1:
        return list

    left, right = split(list)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# Verifies if the list was sorted in ascending order
def verify_ascending_sort(list):
    size = len(list)

    if size == 0 or size == 1:
        return True
    
    return list[0] <= list[1] and verify_ascending_sort(list[1:])

array = [213,54,23,76,3,34,6,7,908,12,213]

print(array)
print(merge_sort(array))
print(verify_ascending_sort(merge_sort(array)))