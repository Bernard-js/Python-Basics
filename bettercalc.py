num1 = float(input('Enter first number: '))
op = input("Enter operator: ")
num2 = float(input('Enter second number: '))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op ==  "/":
    print(num1 / num2)
else:
    print("ERROR! Invalid Operator.")
    print("Use '+', '-', '*', or '/' as valid operators")