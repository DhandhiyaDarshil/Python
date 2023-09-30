# Prompt the user to enter the principal amount, years, and interest rate
principal = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))

# Convert interest rate from percentage to decimal
interest_rate = interest_rate / 100

# Calculate the compound interest
compound_interest = principal * (1 + interest_rate) ** years - principal

# Print the calculated compound interest
print(f"The compound interest after {years} years is: {compound_interest:.2f}")
