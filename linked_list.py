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

#list start with no object
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



# -------------------------------
# 1. Singly Linked List (SLL)
# -------------------------------

class NodeSLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#starts with no object
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = NodeSLL(data)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
    
    def delete(self, target):
        current = self.head
        prev = None
        while current:
            if current.data == target:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def reverse(self):
        prev, current = None, self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        
    def display(self):
        current = self.head
        while current:
            print(curent.data, end =" ->")
            current = current.next
        print("None")
             
# -------------------------------
# 2. Doubly Linked List (DLL)
# -------------------------------

class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __int__(self):
        self.head = None
    
    def insert(self, data):
        new_node = NodeDLL(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
    
    def delete(self, target):
        current = self.head
        while current:
            if current.data == target:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False
    
    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        if prev_node:
            self.head = prev_node.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# -------------------------------
# 3. Circular Singly Linked List (CSLL)
# -------------------------------
class NodeCSLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = NodeCSLL(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def search(self, target):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == target:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def delete(self, target):
        if not self.head:
            return False
        current = self.head
        prev = None
        while True:
            if current.data == target:
                if prev:
                    prev.next = current.next
                else:
                    # deleting head
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:  # single node
                        self.head = None
                    else:
                        self.head = current.next
                        tail.next = self.head
                return True
            prev = current
            current = current.next
            if current == self.head:
                break
        return False

    def reverse(self):
        if not self.head or self.head.next == self.head:
            return
        prev, current = None, self.head
        first = self.head
        while True:
            nxt = current.next
            current.next = prev or self.head
            prev = current
            current = nxt
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# -------------------------------
# 4. Circular Doubly Linked List (CDLL)
# -------------------------------
class NodeCDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = NodeCDLL(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def search(self, target):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == target:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def delete(self, target):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == target:
                if current.next == current:  # only one node
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def reverse(self):
        if not self.head:
            return
        current = self.head
        while True:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            if current == self.head:
                break
        self.head = self.head.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# -------------------------------
# Example Usage
# -------------------------------
print("Singly Linked List:")
sll = SinglyLinkedList()
for i in [10, 20, 30]:
    sll.insert(i)
sll.display()
sll.delete(20)
sll.display()
sll.reverse()
sll.display()

print("\nDoubly Linked List:")
dll = DoublyLinkedList()
for i in [10, 20, 30]:
    dll.insert(i)
dll.display()
dll.delete(20)
dll.display()
dll.reverse()
dll.display()

print("\nCircular Singly Linked List:")
csll = CircularSinglyLinkedList()
for i in [10, 20, 30]:
    csll.insert(i)
csll.display()
csll.delete(20)
csll.display()
csll.reverse()
csll.display()

print("\nCircular Doubly Linked List:")
cdll = CircularDoublyLinkedList()
for i in [10, 20, 30]:
    cdll.insert(i)
cdll.display()
cdll.delete(20)
cdll.display()
cdll.reverse()
cdll.display()

    