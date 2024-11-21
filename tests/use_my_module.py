# File: use_my_module.py

import my_module

# Using the greet function
name = input("Enter a name to greet: ")
greeting = my_module.greet(name)
print(greeting)

# Using the calculate_square function
try:
    number = float(input("Enter a number to square: "))
    result = my_module.calculate_square(number)
    print(f"The square of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Demonstrating that main() from my_module is not executed
print("Note: The main() function from my_module was not executed.")