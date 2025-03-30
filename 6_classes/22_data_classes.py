from collections import namedtuple


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, value):
#         return self.x == value.x and self.y == self.y


Point = namedtuple("Point", ["x", "y"])

# These nametuples are immutable. You cannot modify them after creation
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)  # True
