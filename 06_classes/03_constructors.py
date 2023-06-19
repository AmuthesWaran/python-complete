class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 5)
point1 = Point(2, 5)
# print(point.x)
# print(point.y)
point.z = 10
print(point.z)
point.draw()
