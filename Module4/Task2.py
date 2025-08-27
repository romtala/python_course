
# math_calculations.py

import math

# Ask the user to enter a number
try:
    number = float(input("Enter a number: "))

    # Check if number is valid for sqrt and log
    if number <= 0:
        print("Note: Logarithm and square root require a positive number.")
    else:
        sqrt_result = math.sqrt(number)
        log_result = math.log(number)
        print(f"Square root of {number}: {sqrt_result}")
        print(f"Natural logarithm (ln) of {number}: {log_result}")

    # Sine can be calculated for any real number
    sine_result = math.sin(number)
    print(f"Sine of {number} radians: {sine_result}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
