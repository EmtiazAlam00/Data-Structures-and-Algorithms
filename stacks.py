class Stack:
    def __init__(self):
        self.stack = []

    # Push element to top of stack
    def push(self, item):
        self.stack.append(item)

    # Pop element from top of stack
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack Underflow! Cannot pop from empty stack.")
            return None

    # Peek top element without removing
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Return current size of stack
    def size(self):
        return len(self.stack)

    # Display stack elements
    def display(self):
        print("Stack (top → bottom):", list(reversed(self.stack)))

#-------------