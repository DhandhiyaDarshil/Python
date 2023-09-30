# Prompt the user to enter a number
num = int(input("Enter a positive integer: "))

# Print the divisors
print("Divisors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)