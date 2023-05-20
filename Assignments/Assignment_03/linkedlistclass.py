class LinkedList:

    def __init__(self, a):
        #  Design the constructor based on data type of a. If 'a' is built in python list then
        #  Creates a linked list using the values from the given array. head will refer
        #  to the Node that contains the element from a[0]
        #  Else Sets the value of head. head will refer
        #  to the given LinkedList

        # Hint: Use the type() function to determine the data type of a
        self.head = None
        tail = None
        if type(a) == list:
            for i in a:
                n = Node(i, None)
                if self.head == None:
                    self.head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n
        else:
            self.head = a
    # Traverse elements in the list.
    # This method is done for you. Do not change this method.
    def traverseList(self):
        s = ''
        temp = self.head
        while temp != None:
            if temp.next != None:
                s += str(temp.element) + " "
            else:
                s += str(temp.element)
            temp = temp.next
        return s

    # Count the number of nodes in the list and return the total number
    def countNode(self):
        counter = 0
        currNode = self.head
        while True:
            counter += 1
            if currNode.next != None:
                currNode = currNode.next
            else:
                break
        return counter

    # returns the reference of the Node at the given index. For invalid index return None.
    def nodeAt(self, idx):
        c = self.countNode()
        if idx < 0 and idx > (c - 1):
            return None
        n = self.head
        i = 0
        while i != idx:
            n = n.next
            i += 1
        return n

    # returns the element of the Node at the given index. For invalid idx return None.
    def get(self, idx):

        if idx<0 or idx >= self.countNode():
            return None
        n = self.head
        i = 0
        while i != idx:
            n = n.next
            i += 1
        return n.element

    # updates the element of the Node at the given index.
    # Returns the old element that was replaced. For invalid index return None.
    # parameter: index, element
    def set(self, idx, elem):

        if idx<0 or idx >= self.countNode():
            return None
        currNode = self.nodeAt(idx)
        tmp = currNode.element
        currNode.element = elem
        return tmp

    # returns the index of the Node containing the given element.
    # if the element does not exist in the List, return -1.
    def indexOf(self, elem):

        currNode = self.head
        i = 0
        while i < self.countNode():
            if currNode.element == elem:
                return i
            else:
                currNode = currNode.next
                i += 1

        return -1

    # returns true if the element exists in the List, return false otherwise.
    def contains(self, elem):

        currNode = self.head
        i = 0
        while i < self.countNode():
            if currNode.element == elem:
                return True
            else:
                currNode = currNode.next
                i += 1
        return False

    # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
    def copyList(self):
        # To Do
        # pass
        currNode = None
        newList = None
        tail = None
        i = 0
        while i < self.countNode():
            if newList == None:
                newList = Node(self.head.element, None)
                tail = newList
                i += 1
            else:
                currNode = tail
                tmp = Node(self.get(i), None)
                currNode.next = tmp
                tail = tmp
                i += 1
        return newList

    # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
    def reverseList(self):
        preNode = None
        currNode = self.head
        while currNode != None:
            next = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = next
        self.head = preNode
        return self.head

    # inserts Node containing the given element at the given index
    # Check validity of index. If invalid then print "Invalid Index"
    def insert(self, elem, idx):
        if idx < 0 or idx > self.countNode():
            print("Invalid Index")
            return
        if idx == 0:
            newNode = Node(elem, self.head)
            self.head = newNode
            return
        currNode = self.nodeAt(idx - 1)
        newNode = Node(elem, currNode.next)
        currNode.next = newNode

    # removes Node at the given index. returns element of the removed node.
    # Check validity of index. return None if index is invalid.
    def remove(self, idx):
        if idx < 0 or idx >= self.countNode():
            return None
        if idx == 0:
            elem = self.head.element
            self.head = self.head.next
            return elem
        currNode = self.nodeAt(idx - 1)
        elem = currNode.next.element
        currNode.next = currNode.next.next
        return elem

    # Rotates the list to the left by 1 position.
    def rotateLeft(self):
        if self.countNode() > 1:
            firstNode = self.head
            secondNode = self.head.next
            self.head = secondNode
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = firstNode
            firstNode.next = None

    # Rotates the list to the right by 1 position.
    def rotateRight(self):
        if self.countNode() > 1:
            currNode = self.head
            while currNode.next.next != None:
                currNode = currNode.next
            currNode.next.next = self.head
            self.head = currNode.next
            currNode.next = None
