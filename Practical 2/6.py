# Prompt the user to enter a number
num = int(input("Enter a positive integer: "))

# Calculate the sum of divisors
sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)

# Check if the number is a perfect number
is_perfect = sum_of_divisors == num

# Print the result
if is_perfect:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
