from linked_list import LinkedList

# Slits linked list into two
def split(linked_list: LinkedList):
    if linked_list == None or linked_list.head == None:
        return linked_list, None

    mid = linked_list.size() // 2
    
    mid_node = linked_list.get(mid - 1)

    left = linked_list
    right = LinkedList()
    right.head = mid_node.next
    mid_node.next = None

    return left, right

# Merges two lists into one
def merge(left, right):
    merged = LinkedList()

    # Add fake head, will be discarded later
    merged.preappend(0)

    curr = merged.head

    # Left and Right head nodes
    left_head = left.head
    right_head = right.head

    # Iterate to the end of either list
    while left_head or right_head:
        if left_head is None:
            curr.next = right_head
            # Sets loop condition to false
            right_head = right_head.next
        elif right_head is None:
            curr.next = left_head
            left_head = left_head.next
        else:
            l_data = left_head.data
            r_data = right_head.data

            if l_data < r_data:
                curr.next = left_head
                left_head = left_head.next
            else:
                curr.next = right_head
                right_head = right_head.next
        # Moves to next node
        curr = curr.next

    # Discard fake head
    head = merged.head.next
    merged.head = head

    return merged

# Sorts linked list using merge sort algorithm
def merge_sort(linked_list: LinkedList):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left, right = split(linked_list)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# Homework: write verify function for a linked list merge sort
# Basically just goes to the end of the list and if it does not find any values that are unsorted
# Returns true, because once head.next is not found, true is returned
def verify_merge_ascending(head: None) -> bool:
    # If head is none then returns true, because there is nothing to sort
    if head == None:
        return True
    # If head doesnt have next data, then we assume its sorted and return true
    elif head.next == None:
        return True
    
    # If data is more than next data, return false, list is not sorted
    if head.data > head.next.data:
        return False
    
    # If false was not returned, keep on checking
    return verify_merge_ascending(head.next)

linked_list = LinkedList()
linked_list.preappend(1337)
linked_list.preappend(2)
linked_list.preappend(3)
linked_list.preappend(7331)

# Sorted list
linked_list = merge_sort(linked_list)
print(verify_merge_ascending(linked_list.head))

linked_list1 = LinkedList()
linked_list1.preappend(1)
linked_list1.preappend(2)
linked_list1.preappend(7331)
linked_list1.preappend(3)

# Unsorted list
print(verify_merge_ascending(linked_list1.head))