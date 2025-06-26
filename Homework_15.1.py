# Клас Прямокутник

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if self.get_square() == other.get_square():
            return True
        else:
            return False

    def __add__(self, other):
        sum_rectangles = self.get_square() + other.get_square()
        new_width = self.width
        new_height = sum_rectangles / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if n > 0:
            mul_rectangles = self.get_square() * n
            new_width = self.width
            new_height = mul_rectangles / new_width
            return Rectangle(new_width, new_height)
        else:
            raise ValueError("n - value cannot be negative")

    def __str__(self):
        return f"Rectangle({self.width}), ({self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
print("OK1")
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print("OK2")
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print("OK3")
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("OK4")
