class Point:

    x = 0
    y = 0

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.zero = classmethod(Point.zero)
print(Point.zero())
# print(point.zero())
# print(point.draw())
