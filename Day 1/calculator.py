# basic calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input operation
opr = input("Enter operation (+, -, *, /): ")

# Condition logic
if opr == "+":
    opr = num1 + num2
elif opr == "-":
    result = num1 - num2
elif opr == "*":
    result = num1 * num2
elif opr == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

# Output
print(f"\nResult: {result}")