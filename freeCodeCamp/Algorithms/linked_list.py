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
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = Node(data)

    # Inserts data at a specific index of a linked list
    def insert(self, data, index):
        if index > self.size() or index < 0:
            return

        curr = self.head

        for i in range(index):
            curr = curr.next

        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    # Removes a node from the list at specific index
    def remove(self, index):
        if index > self.size() or index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
            return

        def get_node(index):
            nonlocal self
            node = self.head

            for i in range(index):
                node = node.next

            return node

        curr = get_node(index)
        previous = get_node(index - 1)

        previous.next = curr.next

    # Returns node by index
    def get(self, index):
        if index <= 0:
            return self.head
        
        curr = self.head
        i = 0

        while i < index:
            i += 1
            curr = curr.next
        
        return curr