class Node:
    def __init__(self,value): self.value , self.next= value , None

class Linkedlist:
    def __init__(self): self.head = None        

    def insert(self, value):
        newNode = Node(value)
        if not self.head: self.head = newNode
        else: raise Exception("Sorry, this linkedlist has a head ")

    def includes(self,value):
        if self.head:
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False   
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value ")

    def __str__(self):
        if self.head:
            dataStr, current = '', self.head
            while current:
                dataStr += '{'+str(current.value)+'}-> '
                current = current.next
            dataStr += 'NULL'
            return dataStr
        else: raise Exception("Sorry, list is empty, insert a value ")

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def insertBefore(self,value,newVal):
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                break
            current = current.next
        if current.next is None: raise Exception("the value not exisit ")
        else:
            newNode = Node(newVal)
            newNode.next = current.next
            current.next = newNode

    def insertAfter(self,value,newVal):
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            raise Exception(" the value not exisit ")
        else:
            newNode = Node(newVal)
            newNode.next = current.next
            current.next = newNode
            

if __name__ == "__main__":
        List =Linkedlist()
        List.insert(46)
        List.append(55)
        List.append(66)
        List.append(10)
        List.kthFromEnd(0)
        print(List)       