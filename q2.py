def last4(number):
    
    string = ''
    
    string = str(number)
    last4 = string[count-4:count]
    print("*",end='')
    print(last4)    


num = int(input("Enter the number : "))
count = len(str(num))
last4(num)
