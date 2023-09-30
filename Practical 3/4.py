def add_key_to_dictionary(dictionary, key, value):
    dictionary[key] = value

# Sample dictionary
sample_dict = {0: 10, 1: 20}

# Key and value to add
new_key = 2
new_value = 30

# Add the new key-value pair to the dictionary
add_key_to_dictionary(sample_dict, new_key, new_value)

print("Original Dictionary:", sample_dict)
