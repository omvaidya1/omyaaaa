# Import math module
import math

try:
    # Take a sentence as input
    sentence = input("Enter a sentence: ")

    # Check if the sentence is empty
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")

    # Extract unique words using a set
    unique_words = set(sentence.split())

    # Print unique words in sorted order
    print("\nUnique Words (Sorted):")
    for word in sorted(unique_words):
        print(word)

    # Count unique words
    count = len(unique_words)

    # Print square of the count using math module
    print("\nNumber of unique words:", count)
    print("Square of unique words:", math.pow(count, 2))

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)