def operate(n1, op, n2):
    
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2;
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
operator = input("Enter the operator : ")

print(operate(x, operator, y))