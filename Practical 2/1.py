import sys

if len(sys.argv) < 3:
    print("Usage: python program.py <name> <age>")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])
output = "Name: {}\nAge: {}".format(name, age)
print(output)