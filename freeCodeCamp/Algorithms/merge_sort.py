
# Splits a list into two
def split(list):
    pass

# Merges left and right lists together
def merge(left, right):
    pass

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