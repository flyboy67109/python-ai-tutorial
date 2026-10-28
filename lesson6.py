# Exercise 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

r1 = Rectangle(3, 4)
r2 = Rectangle(5, 2)
print(r1)              # Rectangle(3, 4)
print(r1.area())       # 12
print(r2.area())       # 10
print(r1.perimeter())  # 14

# Exercise 2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)
print(Vector(5, 5) - Vector(1, 2))   # Vector(4, 3)
print(Vector(1, 2) * 3)              # Vector(3, 6)

# Exercise 3
class Value:
    def __init__(self, data, children=()):
        self.data = data
        self.children = children

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other))

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other))

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f"Value({self.data})"

print(Value(5) - Value(2))                 # Value(3)
print(Value(5) - 2)                        # Value(3)
print(sum([Value(1), Value(2), Value(3)])) # Value(6)

# Exercise 4
class Value:
    def __init__(self, data, children=()):
        self.data = data
        self.children = children

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other))

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other))

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __pow__(self, other):
            return Value(self.data ** other, (self,))

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f"Value({self.data})"

print(Value(3) ** 2)    # Value(9)