# factorial_recursive.py

def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Sample call
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
