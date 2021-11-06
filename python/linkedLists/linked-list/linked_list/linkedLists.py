class Node:
    def __init__(self, value):self.value, self.next = value, None

class LinkedList:
    def __init__(self):self.head = None

    def insert(self, value):
        newNode = Node(value)
        newNode.next, self.head = self.head, newNode

    def includes(self, value):
        if self.head is not None:
            current = self.head
            while current:
                if current.value == value: return True
                current = current.next
            return False

    def toString(self):
        if self.head:
            dataStr, current = '', self.head
            while current:
                dataStr += '{'+str(current.value)+'}-> '
                current = current.next
            dataStr += 'NULL'
            return dataStr

