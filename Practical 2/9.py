# Prompt the user to enter the value of N
N = int(input("Enter a positive integer: "))

# Calculate the factorial
factorial = 1
for num in range(2, N + 1):
    factorial *= num

# Print the factorial
print("The factorial of", N, "is:", factorial)