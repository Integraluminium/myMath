from vektor import Vector


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_vektor(self, other: "Point") -> Vector:
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return Vector(x1 - x2, y1 - y2, z1 - z2)

    def get_values(self):
        return self.x, self.y, self.z

    def __getitem__(self, item: int):
        if (item := abs(item)) > 3:
            raise Exception("only the three Values are Indexable")
        return (self.x, self.y, self.z)[item]

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"

    def __eq__(self, other: "Vector") -> bool:
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return x1 == x2 and y1 == y2 and z1 == z2


if __name__ == '__main__':
    p1 = Point(0, 0, 0)
    p2 = Point(1, 2, 2)

    res = p1.get_vektor(p2)
    print(res, res.get_length())
