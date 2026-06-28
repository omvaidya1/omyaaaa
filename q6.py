# Import required modules
import random
import math

# Create an empty set to store unique numbers
numbers = set()

print("Enter 10 numbers:")

# Take 10 numbers as input
for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.add(num)      # Set stores only unique values
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

try:
    # Convert the set into a tuple
    numbers_tuple = tuple(numbers)

    print("\nUnique Numbers (Set):", numbers)
    print("Tuple:", numbers_tuple)

    # Pick and print 3 random numbers from the tuple
    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Less than 3 unique numbers available.")

    # Calculate the sum and its square root
    total = sum(numbers_tuple)

    if total >= 0:
        print("Sum of tuple elements:", total)
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Square root cannot be calculated because the sum is negative.")

except Exception as e:
    print("An error occurred:", e)