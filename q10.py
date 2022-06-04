x = int(input("Enter num 1 : "))
y = int(input("Enter num 2 : "))
print("Values before switching :\n",x,y)
# print()

#swapping using xor

x = x ^ y
y = x ^ y
x = x ^ y

print("Values after switching :\n",x,y)