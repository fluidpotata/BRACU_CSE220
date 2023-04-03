class Node:
    def __init__(self,e,n):
        self.element = e
        self.next = n

d = Node(40,None)
c = Node(30, d)
b = Node(20, c)
a = Node(10, b)

def printSinglyLinkedList(h):
    if h==None:
        return
    printSinglyLinkedList(h.next)
    print(h.element)

printSinglyLinkedList(a)
