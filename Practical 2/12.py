# Print numbers from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("Hum Dum")
    elif num % 3 == 0:
        print("Hum")
    elif num % 5 == 0:
        print("Dum")
    else:
        print(num)
