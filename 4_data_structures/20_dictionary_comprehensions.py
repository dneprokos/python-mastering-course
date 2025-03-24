values = []

# We can use comprehensions
values = [x * 2 for x in range(5)]
print(values)  # [0, 2, 4, 6, 8]

# We can do a simliar and receive a set
values = {x * 2 for x in range(5)}
print(values)  # {0, 2, 4, 6, 8}

# We can also try to make it as a dictionary
values = {x: x * 2 for x in range(5)}
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
