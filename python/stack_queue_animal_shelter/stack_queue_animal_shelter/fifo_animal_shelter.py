class  AnimalShelter :
    def __init__(self) :
        self.frontcat, self.rearcat, self.frontdog, self.reardog = None , None , None , None

    def enqueue(self,animal):
        if "cat" == animal.type :
            if self.frontcat == None : self.frontcat=animal ; self.rearcat=animal
            else: self.rearcat.next=animal ; self.rearcat=animal

        if "dog" == animal.type:
            if self.frontdog == None : self.frontdog=animal ; self.reardog=animal
            else: self.reardog.next=animal ; self.reardog=animal



    def dequeue(self,pref):
        if "cat" == pref and self.frontcat != None :
            temp = self.frontcat ; self.frontcat=temp.next ; temp.next=None
            return temp.name

        elif "dog" == pref and self.frontdog != None :
            temp=self.frontdog ; self.frontdog = temp.next ; temp.next = None
            return temp.name 
        else: return 'null'       


class Cat():
    def __init__(self,name):
        self.name, self.type, self.next=name, 'cat', None

class Dog():
    def __init__(self,name):
        self.name, self.type, self.next=name, 'dog', None