def variable_length_func(*args):
    print('#'.join(map(str, args)))

# Test the function
variable_length_func(1, 2, 3, 4, 5)
variable_length_func('a', 'b', 'c', 'd')
variable_length_func(True, False, True)
X