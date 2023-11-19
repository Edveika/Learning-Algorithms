def binary_search(list, target):
    if not len(list):
        return False
    
    middle = (len(list)) // 2

    if list[middle] == target:
        return True
    elif list[middle] < target:
        # +1 because the target is bigger than the middle, so it gets assigned to the other half
        return binary_search(list[middle + 1:], target)
    else:
        # -1 is not needed, because upper statement deals with this logic
        # if middle is smaller it gets added to this smaller list
        return binary_search(list[:middle], target)

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 4))