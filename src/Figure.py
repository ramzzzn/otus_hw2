from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def add_area(self, second_figure):
        if isinstance(second_figure, Figure):
            return round(self.calculate_area() + second_figure.calculate_area(), 2)
        raise ValueError(f'Object {second_figure} is not figure')
