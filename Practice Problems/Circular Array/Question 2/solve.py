n = 5
arr = [1, 6, 4, 3, 5]
newArray = [-1]*5
for i in range(5):
    for j in range(5):
        if arr[(i+j)%5]>arr[i]:
            newArray[i] = arr[(i+j)%5]
            break

print(newArray)
