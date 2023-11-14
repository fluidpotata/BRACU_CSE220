#Using Linked List
class ListStack:
    def __init__(self):
      self.size=0
      self.top=None

    #Returns The number of items on the stack
    def size(self):
      return self.size

    #Returns true if the stack is empty
    def isEmpty(self):
      if(self.size==0):
        return True
      return False

    #Pushes the new item on the stack
    def push(self,e):
        pass
    
    #Pops the item on the top of the stack
    def pop(self):
        pass
    #Returns the item on the top of the stack
    def peek(self):
        pass

    #Print all items of the stack 
    def listPrint(self):
      t=self.top
      while(t!=None):
          print(t.element,end="")
          t=t.next
