d = {'British raj': 200,
    'Mughal empire': 350,
    'Delhi sultanate': 100,
    'Maurya Empire': 150}

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

print("Original Dictionary:", d)
print("Sorted Dictionary:", sorted_d)
