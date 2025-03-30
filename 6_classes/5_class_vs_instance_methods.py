class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        return print(f"Point({self.x}, {self.y})")


point = Point.zero()
print(point.draw())  # Point(0, 0)
