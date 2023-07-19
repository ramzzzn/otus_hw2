import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError(f'Cannot create rectangle')
        self.radius = radius
        self.name = 'Circle'

    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
