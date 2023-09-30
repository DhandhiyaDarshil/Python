def sum_dictionary_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Example dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}

# Calculate the sum of values in the dictionary
total = sum_dictionary_values(my_dict)

print("Dictionary:", my_dict)
print("Sum of Values:", total)
