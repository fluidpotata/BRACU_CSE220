def check_duplicate(root,arr=[]):
    if root==None:
        return
    if root.element in arr:
        return True
    else:
        arr.append(root.element)
    check_duplicate(root.left)
    check_duplicate(root.right)
    return False

