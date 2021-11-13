from stack_and_queue.node import Node

class Queue():
    def __init__(self):
        self.front = None ; self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node ; self.rear = node
        else: self.rear.next = node ; self.rear = node

    def dequeue(self):
        try: self.front.value
        except: return "Queue is Empty"
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    def peek(self):
        try: return self.front.value
        except: return "Queue is Empty"

    def isEmpty(self):
        if self.front == None and self.rear == None: return True
        else: return False


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(5) ; queue.enqueue(6)
    queue.enqueue(7) ; queue.dequeue()
    
    print(queue.front.value)
