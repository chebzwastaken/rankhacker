import math
class Rectangle:
    def __init__(self, length, height) -> None:
        self.length = length
        self.height = height

    def area(self):
        area = self.height * self.length
        return area

class Circle:
    
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    

c = Circle(math.pi)
print(c.area())

