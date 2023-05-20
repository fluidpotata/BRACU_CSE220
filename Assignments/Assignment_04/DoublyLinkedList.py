from DoublyNode import Node as doublyNode


class DoublyList:

    def __init__(self, a):
        # Creates a Non Dummy Headed Circular Doubly Linked List using the values from the given array a.
        # To Do
        self.head = None
        tail = None
        for i in range(len(a)):
            n = doublyNode(a[i],None,None)
            if self.head == None:
                self.head = n
                tail = n
            else:
                n.prev = tail
                tail.next = n
                tail = n
            tail.next = self.head
            self.head.prev = tail

    # Counts the number of Nodes in the list and return the number
    def countNode(self):
        # To Do
        counter = 0
        temp = self.head
        while True:
            counter+=1
            if temp.next==self.head:
                break
            temp = temp.next
        return counter

    # prints the elements in the list
    def forwardprint(self):
        # To Do
        printstate = ""
        temp = self.head.next
        printstate+= str(self.head.element)+" "
        while temp != self.head:
            printstate += str(temp.element).join(", ")
            temp = temp.next
        print(printstate+".")
    # prints the elements in the list backward
    def backwardprint(self):
        # To Do
        printstate = ""
        temp = self.head.prev
        while True:
            printstate += str(temp.element).join(", ")
            if temp==self.head:
                break
            temp = temp.prev
        printstate = printstate[1:]
        print(printstate+".")

    # returns the reference of the at the given index. For invalid index return None.
    def nodeAt(self, idx):
        # To Do
        currNode = self.head
        counter = 0
        while True:
            if counter==idx:
                return currNode
            else:
                counter += 1
                currNode = currNode.next
            if currNode == self.head:
                break
        return doublyNode("Index error",None,None)

    # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        # To Do
        counter = 0
        currNode = self.head
        while True:
            if currNode.element == elem:
                return counter
            else:
                counter+=1
                currNode = currNode.next
            if currNode==self.head:
                break

        return -1

    # inserts containing the given element at the given index Check validity of index.
    def insert(self, elem, idx):
        # To Do
        if idx<0 or idx>self.countNode():
            print("Invalid index")
            return
        n = doublyNode(elem, None, None)
        if idx==self.countNode():
            prevNode = self.nodeAt(idx-1)
            n.next = prevNode.next
            prevNode.next.prev = n
            prevNode.next = n
            n.prev = prevNode
        else:
            currNode = self.nodeAt(idx)
            n.next = currNode
            n.prev = currNode.prev
            n.prev.next = n
            currNode.prev = n
        if idx == 0:
            self.head = n


    # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
    def remove(self, idx):
        # To Do
        if idx<0 or idx>=self.countNode():
            print("Invalid index")
            return
        currNode = self.nodeAt(idx)
        if idx == 0:
            self.head = currNode.next
        currNode.next.prev = currNode.prev
        currNode.prev.next = currNode.next
        return str(currNode.element)
