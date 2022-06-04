# to check a palindromic string

string = input("Enter the string :")
if string == string[::-1]:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")