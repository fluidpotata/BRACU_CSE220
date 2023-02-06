def inputChecker(s1,s2):
    if len(s1)>10 or len(s2)>10:
        return True
    else:
        return False
def startChecker(s1):
    for i in range(len(s1)):
        if 65 <= ord(s1[i]) <= 90:
            return i
def rotateLeft(source):
    length = len(source)
    tmp = source[0]
    for i in range(len(source)-1):
        source[i] = source[i+1]
    source[len(source)-1] = tmp

    return source

def rotateRight(source):
    j = len(source) - 1
    while True:
        if source[j-1]!='':
            tmp = source[j-1]
            j-=1
            break
        j-=1
    # j = len(source) - 1
    while j > 0:
        source[j%len(source)] = source[(j - 1)%len(source)]
        j -= 1
    source[0] = tmp

    return source

def printArray(arr):
    x = ""
    for i in arr:
        if i!="":
            x+=i
    print(x)

def defaultPrint(s1,n1,s2,n2):
    print(f"Top Board Start Character: {strtchr1}")
    print(f"Top Board Start Index: {strt1}")
    print(f"Bottom Board Start Character: {strtchr2}")
    print(f"Top Board Start Index: {strt2}")

mul_array = [[""]*10, [""]*10]
topsent = input(" ")
botsent = input(" ")

if inputChecker(topsent, botsent):
    print("Invalid Input")
else:
    strt1, strt2 = startChecker(topsent),  startChecker(botsent)

    n1,n2 = strt1,strt2
    for i in range(len(botsent)):
        mul_array[1][i] = botsent[n2]
        n2 = (n2+1)%len(botsent)

    for j in range(len(topsent)):
        mul_array[0][j] = topsent[n1]
        n1 = (n1-1)%len(topsent)
        if n1<0:
            n1 = len(topsent)-1

    strtchr1, strtchr2 = mul_array[0][0], mul_array[1][0]
    print(f"Your input is valid. Press any key and enter to continue!!!")
    defaultPrint(strtchr1,strt1,strtchr2,strt2)
    chck = input("")
    while True:
        if chck=='Q' or chck=='q':
            break
        printArray(mul_array[0])
        printArray(mul_array[1])
        rotateLeft(mul_array[0])
        rotateRight(mul_array[1])
        defaultPrint(strtchr1, strt1, strtchr2, strt2)
        chck = input("Press any key and enter to continue!!!")
    defaultPrint(strtchr1, strt1, strtchr2, strt2)
