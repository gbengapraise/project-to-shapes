from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height



class Square(Polygon):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height



def main():
    rectangle = Rectangle(10, 5)
    square = Square(4)
    triangle = Triangle(6, 8)

    shapes = [rectangle, square, triangle]

    for shape in shapes:
        area = shape.calculate_area()
        if isinstance(shape, Rectangle):
            print(f"Rectangle area: {area}")
        elif isinstance(shape, Square):
            print(f"Square area: {area}")
        elif isinstance(shape, Triangle):
            print(f"Triangle area: {area}")


if __name__ == "__main__":
    main()


