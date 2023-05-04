# 1-4

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __mul__(self, number: int):
        self.x *= number
        self.y *= number
        return self

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False


punkt = Point()
punkt.x = 2
punkt.y = 1

punkt2 = Point()
punkt2.x = 2

print(punkt.__eq__(punkt2))


# zad 5-7

class Polygon:

    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        return self.points.append(point)

    def __str__(self):
        points_list = ", ".join([f"Point({p.x}, {p.y})" for p in self.points])
        return f"Polygon[{points_list}]"

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            new_poly = Polygon()
            new_poly.points = self.points[item]
            return new_poly
        else:
            raise TypeError("Item musi być typu int lub slice")


poly = Polygon()
poly.add_point(punkt)
poly.add_point(punkt2)
poly.add_point(Point())

print(poly[1:3])
