def concatenate_dictionaries(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict.update(d)
    return concatenated_dict

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries
result_dict = concatenate_dictionaries(dic1, dic2, dic3)

print("Dictionary 1:", dic1)
print("Dictionary 2:", dic2)
print("Dictionary 3:", dic3)
print("Concatenated Dictionary:", result_dict)
