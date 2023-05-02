def print_Ancestor(node):
    if node.parent==None:
        return
    print(node.parent.element)
    print_Ancestor(node.parent)
