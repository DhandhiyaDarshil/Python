# Prompt the user to enter a value in centimeters
centimeters = float(input("Enter a value in centimeters: "))

# Convert centimeters to meters and inches
meters = centimeters / 100
inches = centimeters / 2.54

# Print the converted values
print(f"{centimeters} centimeters is equal to {meters:.2f} meters.")
print(f"{centimeters} centimeters is equal to {inches:.2f} inches.")
