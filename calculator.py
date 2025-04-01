# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+': #Addition operation
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-': #Subraction operation
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*': #Multiplication operation
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/': #Division operation
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation! Please use +, -, *, or /")