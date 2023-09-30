def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries
merged_dict = merge_dicts(dict1, dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)
