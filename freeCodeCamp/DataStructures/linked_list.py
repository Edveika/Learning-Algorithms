# Structure of a singly linked list
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    # Returns a string that contains the data of the node
    def __repr__(self):
        return "Node data: " + str(self.data)
    
n1 = Node(1337)
print(n1)