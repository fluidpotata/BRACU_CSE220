def printTree(val,i=0):
    if val==i:
        return
    printTree(val-1)
    for j in range(1,val+1):
        print(j,end=" ")
    print()
    return
printTree(5)
