class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 5)
other = Point(5, 6)

print(point)
print(other)

print(type(3))
print(type(3))

print(point == other)

print(point < other)
