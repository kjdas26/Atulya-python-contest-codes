numbers = eval(input("Enter the array : "))

frequency = {}
count = 0

for keys in numbers:
    if keys not in frequency:
        count = numbers.count(keys)
        frequency[keys] = count

# print(frequency)

max = -999
for key in frequency:
    if frequency[key] > max:
        max = frequency[key]
        max_ele = key
       
print("Element with max frequency :",max_ele)

