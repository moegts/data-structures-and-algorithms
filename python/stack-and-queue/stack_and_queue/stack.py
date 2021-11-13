from stack_and_queue.node import Node


class Stack:
    
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)

        if self.top: node.next = self.top ; self.top = node
        else: self.top = node

    def pop(self):
        try:
            deletedValue = self.top.value
            temp = self.top.next
            self.top = temp
            temp.next = None
            return deletedValue
        except: return "Stack is Empty"

    def peek(self):
        try: return self.top.value
        except: return "Stack is Empty"

    def isEmpty(self):
        if self.top == None: return False
        else: return True

if __name__ == "__main__":
    stack = Stack()

    stack.push(4) ; stack.push(1)
    stack.push(2) ; stack.push(15)
    stack.push(25)
    pop = stack.pop() ; peek = stack.peek()

    print(peek)