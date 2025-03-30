class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(1, 2)
point.z = 10  # Dynamic attributes. We can define after class creation
print(point.draw())  # Point(1, 2)

another = Point(3, 4)  # Another instance
print(another.draw())  # Point(3, 4)

# Instance memeber
print(point.default_color)  # red
print(Point.default_color)  # red

# Change instance member
Point.default_color = "green"
print(point.default_color)  # green
print(Point.default_color)  # green
