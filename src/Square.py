from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(f'Cannot create square')
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = 'Square'
