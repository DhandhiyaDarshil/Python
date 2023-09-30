# Prompt the user to enter the number of rows and columns
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Calculate the value of r (last three digits of your Roll no.)
r = 80  # Replace with your Roll no.'s last three digits

# Generate the two-dimensional array
array = [[i * j * r for j in range(n)] for i in range(m)]

# Print the generated array
print("Generated array:")
for row in array:
    print(row)