# Prompt the user to enter a number
num = int(input("Enter a positive integer: "))

# Check if the number is prime
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# Print the result
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
