def printArray(a,i=0):
    if i==len(a):
        return
    print(a[i])
    printArray(a,i+1)

a = [10,20,30,40,50]
printArray(a)
