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


linked_list = LinkedList()

linked_list.preappend(1337)
linked_list.preappend(2)
linked_list.preappend(3)
linked_list.preappend(7331)

linked_list = merge_sort(linked_list)