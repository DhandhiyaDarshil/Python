# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize variables
letter_count = 0
digit_count = 0

# Calculate the number of digits and letters
for char in string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# Print the results
print("Letters:", letter_count)
print("Digits:", digit_count)