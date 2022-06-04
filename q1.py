def numbers(lst, order):
    
    if order == 'desc':
        lst.sort()
        lst.reverse()
        return lst
    
    if order == 'asc':
        lst.sort()
        return lst
    
    if order == 'none':
        return lst
    
list = eval(input("Enter the list : "))
command = input("Enter the command : ")

result = numbers(list, command)
print("The result is",result)