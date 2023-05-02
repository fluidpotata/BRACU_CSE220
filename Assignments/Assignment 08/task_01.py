from main import Node

def identical(root1, root2):
    if root1==None and root2==None:
        return True
    elif root1==None or root2==None:
        return False
    else:
        return (root1.element == root2.element) and identical(root1.left, root2.left) and identical(root1.right, root2.right)
bt1 = Node(1)
node3 = Node(3)
node2 = Node(2)
bt1.left = node2
bt1.right = node3


bt2 = Node(1)
node6 = Node(3)
node5 = Node(2)
bt2.left = node6
bt2.right = node5

print(identical(bt1,bt2))