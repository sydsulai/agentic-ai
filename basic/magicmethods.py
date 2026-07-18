class ComplexNumbers:
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        real_part = self.real * other.real - self.image * other.image
        image_part = self.real * other.image + self.image * other.real
        return ComplexNumbers(real_part, image_part)
    
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.image ** 2
        real_part = (self.real * other.real + self.image * other.image) / denominator
        image_part = (self.image * other.real - self.real * other.image) / denominator
        return ComplexNumbers(real_part, image_part)
    
    def __repr__(self):
        return f"{self.real} + {self.image}i"
    
if __name__ == "__main__":
    c1 = ComplexNumbers(2, 3)
    c2 = ComplexNumbers(1, 4)
    
    print("Addition:", c1 + c2)
    print("Subtraction:", c1 - c2)
    print("Multiplication:", c1 * c2)
    print("Division:", c1 / c2)