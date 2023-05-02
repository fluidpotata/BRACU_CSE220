from main import Node


class binary_search_tree:
    def __init__(self):
        self.root = None


    def createBinaryTree(self, arr):
        for i in arr:
            n = Node(i)
            self.insertNode(self.root, n)

    def insertNode(self, root, node):
        if self.root is None:
            self.root = node
        else:
            if node.element < root.element:
                if root.left is None:
                    root.left = node
                    root.left.parent = root
                else:
                    self.insertNode(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                    root.right.parent = root
                else:
                    self.insertNode(root.right, node)

    def level(self, node):
        if node.parent is None:
            return 0
        return 1 + self.level(node.parent)

    def height(self,root="Start"):
        if root == "Start":
            root=self.root
        if root is None:
            return -1
        return 1+ max(self.height(root.left),self.height(root.right))

    @staticmethod
    def preOrderPrint(root):
        if root is None:
            return
        print(root.element)
        binary_search_tree.preOrderPrint(root.left)
        binary_search_tree.preOrderPrint(root.right)

    def inOrderPrint(self,root="Undefined"):
        if root == "Undefined":
            root = self.root
        if root is None:
            return
        self.inOrderPrint(root.left)
        print(root.element)
        self.inOrderPrint(root.right)

    def postOrderPrint(self, root = "Undefined"):
        if root == "Undefined":
            root = self.root
        if root is None:
            return
        self.postOrderPrint(root.left)
        self.postOrderPrint(root.right)
        print(root.element)
    def countNodes(self,root="Undefined"):
        if root == "Undefined":
            root = self.root
        if root == None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def arrTree(self):
        self.arr = [0]*(2**(self.height()+1))
        self.createarrTree()

    def createarrTree(self,root = "root", n=1):
        if root == "root":
            root = self.root
        if root is None:
            return
        self.arr[n] = root.element
        self.createarrTree(root.left, 2*n)
        self.createarrTree(root.right, 2*n+1)



print("+++++++++++++++++++")
a = [70,30,23,45,85,75,90,27,77]
b = binary_search_tree()
b.createBinaryTree(a)
# b.preOrderPrint(b.root)
# b.inOrderPrint()
# b.postOrderPrint()
arr = [0]*b.countNodes()
b.arrTree()
print(b.arr)
