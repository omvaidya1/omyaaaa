# Lambda function to calculate the square of a number
square = lambda x: x ** 2

try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)

    # Store squares in a list using the lambda function
    squares = [square(num) for num in numbers]

    # Print all squares
    print("Squares of numbers from 1 to 20:")
    print(squares)

    # Print only the even squares
    print("\nEven Squares:")
    for sq in squares:
        if sq % 2 == 0:
            print(sq, end=" ")

except Exception as e:
    print("An error occurred:", e)