# basic_math_operations.py

# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully (avoid division by zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
