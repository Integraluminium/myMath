import math


class Vector:
    def __init__(self, x: [int, float], y: [int, float], z: [int, float]):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector") -> "Vector":
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return Vector(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other: "Vector") -> "Vector":
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return Vector(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, other: int) -> "Vector":
        x1, y1, z1 = self.get_values()
        return Vector(x1*other, y1*other, z1*other)

    def __truediv__(self, other) -> "Vector":
        x1, y1, z1 = self.get_values()
        return Vector(x1/other, y1/other, z1/other)
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other: "Vector") -> bool:
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return x1 == x2 and y1 == y2 and z1 == z2

    def __abs__(self) -> float:
        return self.get_length()

    def __getitem__(self, item: int):
        if (item := abs(item)) > 3:
            raise Exception("only the three Values are Indexable")
        return (self.x, self.y, self.z)[item]

    def multiply_scalar(self, scalar: int) -> "Vector":
        return self * scalar

    def cross_product(self, other: "Vector") -> "Vector":
        a, b, c = self.get_values()
        d, e, f = other.get_values()
        x = (b*f) - (c*e)
        y = (c*d) - (a*f)
        z = (a*e) - (b*d)
        return Vector(x, y, z)

    def get_values(self):
        return self.x, self.y, self.z

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        return self/abs(self)


if __name__ == '__main__':
    v = Vector(1, 2, 2)
    print(abs(v))
    w, e, r = v
    print(*v)
    print(v)
    print(a := v.normalize())
    print(a.get_length())
