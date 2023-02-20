n = 5
nums = [1, 6, 4, 3, 5]
newArray = [-1]*5
for i in range(5):
    for j in range(5):
        if nums[(i+j)%5]>nums[i]:
            newArray[i] = nums[(i+j)%5]
            break

print(newArray)
