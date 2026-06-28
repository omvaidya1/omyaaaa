def analyze_string(s):
    # Handle empty string
    if len(s) == 0:
        print("The string is empty.")
        return

    # Print length
    print("Length of the string:", len(s))

    # Print reversed string
    print("Reversed string:", s[::-1])

    # Count vowels (case-insensitive)
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)

    # Print each character with positive and negative index
    print("\nCharacter\tPositive Index\tNegative Index")
    for i in range(len(s)):
        print(f"{s[i]}\t\t{i}\t\t{i - len(s)}")


# User input
text = input("Enter a string: ")
analyze_string(text)