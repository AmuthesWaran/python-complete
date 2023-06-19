class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Class level attribute
Point.default_color = "Blue"
point = Point(1, 5)
point1 = Point(2, 5)
# Object level attribute
point1.default_color = "Green"
print(point.default_color)
print(point1.default_color)
print(Point.default_color)
# print(point.x)
# print(point.y)
point.z = 10
print(point.z)
point.draw()
