from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Cannot create rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def calculate_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def calculate_area(self):
        return self.side_a * self.side_b
