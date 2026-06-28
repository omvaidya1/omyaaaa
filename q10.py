# Import math module
import math

# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                print("Result =", num1 / num2)

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter valid numeric values.")


# Function for Scientific Calculations
def scientific_calculator():
    try:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Square root of a negative number is not possible.")
            else:
                print("Square Root =", math.sqrt(num))

        elif choice == 2:
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Power =", math.pow(base, exponent))

        elif choice == 3:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print("Factorial =", math.factorial(num))

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# Main Menu
while True:
    print("\n====== Smart Calculator & Data Manager ======")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Exit")

    try:
        option = int(input("Enter your choice: "))

        if option == 1:
            basic_arithmetic()

        elif option == 2:
            scientific_calculator()

        elif option == 3:
            print("Thank you! Program Ended.")
            break

        else:
            print("Please choose a valid option.")

    except ValueError:
        print("Invalid input! Please enter a number.")