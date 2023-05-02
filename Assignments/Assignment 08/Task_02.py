class Node:
    def __init__(self,e,l=None,r=None):
        self.element = e
        self.left = l
        self.right = r

def mirror_converter(root):
    if root==None:
        return
    temp = root.right
    root.right = root.left
    root.left = temp
    mirror_converter(root.left)
    mirror_converter(root.right)
    return root


node4 = Node(40)
node5 = Node(60)
node2 = Node(20,node4)
node3 = Node(30,None,node5)
root = Node(10,node2,node3)
print(root.left.element)

nroot = mirror_converter(root)
print(nroot.left.left.element)