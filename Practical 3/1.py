def check_key_in_dictionary(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# Example dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Key to check
key_to_check = 'age'

# Check if the key exists in the dictionary
if check_key_in_dictionary(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")