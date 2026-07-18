import math

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(5)]
    
    for shape in shapes:
        print(f"The area of the {shape.name} is {shape.area()}.")