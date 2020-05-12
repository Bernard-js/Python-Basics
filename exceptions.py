
try:
    value = 38/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("You broke the math rules! cannot divide by zero")
except ValueError:
    print("Invalid input, try using an integer")
