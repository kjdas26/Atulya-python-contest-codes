string = input("Enter the string : ")
string_list = []

for letters in string:
    string_list.append(letters)

string_list.sort()
string2 = ''
for words in string_list:
    string2 += words

print("The updated string is :",string2)