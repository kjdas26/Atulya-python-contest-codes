import random

arr = []

for i in range(100):
    num = random.randint(1,99)
    arr.append(num)
    
arr.sort()
# time compexity of this function is O(n*logn)
duplicates = []

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        if arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements :")
print(duplicates)