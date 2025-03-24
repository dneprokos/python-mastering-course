# Dictionary init
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# Access value by key
print(point["x"])  # 1

# Change value by key
point["x"] = 10
print(point["x"])  # 10

# add new key
point["z"] = 20
print(point)  # {'x': 10, 'y': 2, 'z': 20}

# if try to access key does not exist - we will receive an error

# We can verify if key exists
if "a" in point:
    print(point["a"])

# Or we canuse a get function and return default value if does not exist
print(point.get("a", 0))  # 0

# Delete item
del point["x"]
print(point)  # {'y': 2, 'z': 20}


# Loop over dictionaries
for key in point:
    print(key, point[key])
    # y 2
    # z 20

# Iterate and receive tuple
for x in point.items():
    print(x)
# ('y', 2)
# ('z', 20)

# Or we can unpcak it
for key, value in point.items():
    print(key, value)
# y 2
# z 20
