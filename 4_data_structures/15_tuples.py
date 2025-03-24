# Tuple is read-only list
# We cannot modify it

# Tuple initialization
point1 = (1, 2)
point2 = 1, 2
point3 = 1,
point4 = ()

print(type(point1))  # <class 'tuple'>
print(type(point2))  # <class 'tuple'>
print(type(point3))  # <class 'tuple'>
print(type(point4))  # <class 'tuple'>

tuple_concut = (1, 2) + (3, 4)
print(tuple_concut)  # (1, 2, 3, 4)

tuple_multiply = (1, 2) * 3
print(tuple_multiply)  # (1, 2, 1, 2, 1, 2)

my_tuple = tuple([1, 2])
print(my_tuple)  # (1, 2)

my_tuple = tuple("Hello World")
print(my_tuple)  # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

test = (1, 2, 3)

# Access by index
print(test[0])  # 1

# Access range of items
print(test[0:2])  # (1, 2)

# decomposition
x, y, z = test
print(z)  # 3

# Find in tuple
if 2 in test:
    print("Found")  # Found

# Tuples is better to use when you want to avoid collection modification
