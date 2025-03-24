numbers = [1, 2, 3]

print(numbers)  # [1, 2, 3]
# unpacking individual elements
print(*numbers)  # 1 2 3

values = [*range(5), *"Hello"]
print(values)  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

first = [1, 2]
second = [3, 5]
# Combine list using unpacking
combined_lists = [*first, *second]
print(combined_lists)  # [1, 2, 3, 5]

# Combine dictionaries
dict1 = dict(x=1, y=2)
dict2 = dict(x=10, z=5)

# When key is the same, then the last value will be used
combined_dict = {**dict1, **dict2, "w": 7}
print(combined_dict)  # {'x': 10, 'y': 2, 'z': 5, 'w': 7}
