# Prompt the user to enter an integer
num = input("Enter an integer: ")

# Calculate the sum of digits
sum_of_digits = sum(int(digit) for digit in num)

# Print the sum of digits
print("Sum of digits:", sum_of_digits)
