# Prompt the user to enter the value of N
N = int(input("Enter the value of N: "))

# Initialize the first two numbers in the series
num1, num2 = 0, 1

# Print the first N numbers in the Fibonacci series
print("Fibonacci series:")
for _ in range(N):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2
