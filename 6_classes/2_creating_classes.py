class Point:
    def draw(self):  # By default each method should have self parameter
        print("draw")


point = Point()
print(type(point))  # <class '__main__.Point'>
point.draw()  # draw
print(isinstance(point, Point))  # True
