string = input("Enter a string : ")
sum = 0

for letter in string:
    if letter.isnumeric():
        sum += int(letter)

print(sum)