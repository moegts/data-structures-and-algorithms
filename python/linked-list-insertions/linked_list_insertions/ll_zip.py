from linked_list_insertions.linked_list import Linkedlist

def zip_Lists(listOne, listTwo):
    currentOne, currentTwo = listOne.head, listTwo.head

    if not currentOne: 
        listOne.head = listTwo.head
        return listOne.head
    if not currentTwo: return listOne.head

    pointer = currentTwo.next

    while currentOne.next and currentTwo.next:
        currentTwo.next = currentOne.next
        currentOne.next= currentTwo
        currentOne = currentTwo.next
        currentTwo = pointer
        pointer = pointer.next


    if not currentOne.next: 
        currentOne.next = currentTwo
        return listOne.head

    if not currentTwo.next:
        currentTwo.next = currentOne.next
        currentOne.next = currentTwo
        return listOne.head
        

if __name__ == "__main__":
    llOne, llTwo = Linkedlist(), Linkedlist()
    llOne.append(10) ; llOne.append(34)
    llTwo.append(42) ; llTwo.append(54)
    llTwo.append(57) ; llTwo.append(64)
    print(llOne.__str__()) ; print(llTwo.__str__())
    zip_Lists(llOne,llTwo) ; print(llOne.__str__())