from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        if (side_a <= 0 or side_b <= 0 or side_c <= 0) or (
                side_b + side_c <= side_a or side_b >= side_a + side_c or side_c >= side_a + side_b):
            raise ValueError(f'Cannot create rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'Triangle'

    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def calculate_area(self):
        p = self.calculate_perimeter() / 2
        return round(math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2)
