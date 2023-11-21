# Structure of a singly linked list
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    # Returns a string that contains the data of the node
    def __repr__(self) -> str:
        return "Node data: " + str(self.data)
    
class LinkedList:
    head: Node  = None

    def __init__(self):
        self.head = None

    # Returns true if linked list is empty
    # Returns false if linked list is not empty
    def is_empty(self) -> bool:
        return self.head == None
    
    # Returns number of elements in the linked list
    def size(self) -> int:
        curr = self.head
        size = 0

        while curr:
            size += 1
            curr = curr.next

        return size
    
    # Adds data at the beggining of the list
    def preappend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Adds data to the end of the list
    def append(self, data):
        curr = self.head

        while curr:
            curr = curr.next

        curr.data = data