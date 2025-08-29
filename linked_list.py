#determined by pointers
#use cases
#implement other data structures: stacks, queues, hash table
#dynamic memory allocation
#head and tail
#Operations: search, insert, delete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def insert(self, node):
        # insert at the beginning
        node.next = self.head
        if self.head:
            self.head.prev = node   # <-- fix: use the passed node, not class Node
        self.head = node

    def delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = LinkedList()

# Insert nodes
dll.insert(Node(10))
dll.insert(Node(20))
dll.insert(Node(30))

dll.display()  # 30 <-> 20 <-> 10 <-> None

# Search for a node
found = dll.search(20)
print("Found:", found.data if found else "Not Found")

# Delete a node
dll.delete(found)

dll.display()  # 30 <-> 10 <-> None
