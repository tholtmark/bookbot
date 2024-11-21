# File: my_module.py

def greet(name):
    return f"Hello, {name}!"

def calculate_square(number):
    return number ** 2

def main():
    print("Running the script directly!")
    name = input("Enter your name: ")
    print(greet(name))
    
    num = float(input("Enter a number to square: "))
    print(f"The square of {num} is {calculate_square(num)}")

if __name__ == "__main__":
    main()
else:
    print("The module is being imported")