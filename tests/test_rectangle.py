import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestRectangle:
    @pytest.mark.parametrize('side_a, side_b, perimeter, area',
                             [
                                 (1, 2, 6, 2),
                                 (10, 20, 60, 200),
                                 (50, 100, 300, 5000),
                             ])
    def test_rectangle(self, side_a, side_b, perimeter, area):
        """
        Проверка вычисления площади и периметра для фигуры "Прямоугольник"
        """
        r = Rectangle(side_a, side_b)
        assert r.name == 'Rectangle'
        assert r.calculate_perimeter() == perimeter
        assert r.calculate_area() == area

    @pytest.mark.parametrize('side_a, side_b',
                             [
                                 (-7, -4),
                                 (0, 0),
                                 (8, 0),
                                 (0, 9),
                             ])
    def test_rectangle_negative(self, side_a, side_b):
        """
        Проверка вывода ошибки создания фигуры "Прямоугольник"
        """
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)

    @pytest.mark.parametrize('side_a, side_b, side_a1, side_b1, result',
                             [
                                 (10, 2, 10, 20, 220),
                             ])
    def test_add_area_rectangle(self, side_a, side_b, side_a1, side_b1, result):
        """
        Проверка вычисления суммы площадей для фигуры "Прямоугольник"
        """
        r1 = Rectangle(side_a, side_b)
        r2 = Rectangle(side_a1, side_b1)
        assert r1.add_area(r2) == result

    @pytest.mark.parametrize('side_a, side_b, side_a1, result',
                             [
                                 (10, 2, 10, 120),
                             ])
    def test_add_area_rectangle_w_square(self, side_a, side_b, side_a1, result):
        """
        Проверка вычисления суммы площадей для фигур "Прямоугольник" и "Квадрат"
        """
        r = Rectangle(side_a, side_b)
        s = Square(side_a)
        assert r.add_area(s) == result

    @pytest.mark.parametrize('side_a, side_b, radius, result',
                             [
                                 (10, 2, 10, 334.16),
                             ])
    def test_add_area_rectangle_w_circle(self, side_a, side_b, radius, result):
        """
        Проверка вычисления суммы площадей для фигур "Прямоугольник" и "Круг"
        """
        r = Rectangle(side_a, side_b)
        c = Circle(radius)
        assert r.add_area(c) == result

    @pytest.mark.parametrize('side_a, side_b, side_a1, side_b1, side_c1, result',
                             [
                                 (10, 2, 10, 15, 20, 92.62),
                             ])
    def test_add_area_rectangle_w_triangle(self, side_a, side_b, side_a1, side_b1, side_c1, result):
        """
        Проверка вычисления суммы площадей для фигур "Прямоугольник" и "Треугольник"
        """
        r = Rectangle(side_a, side_b)
        t = Triangle(side_a1, side_b1, side_c1)
        assert r.add_area(t) == result

    @pytest.mark.parametrize('side_a, side_b',
                             [
                                 (10, 2),
                             ])
    def test_add_area_rectangle_negative(self, side_a, side_b):
        """
        Проверка вывода ошибки вычисления суммы площадей для фигуры "Прямоугольник"
        """
        r = Rectangle(side_a, side_b)
        with pytest.raises(ValueError):
            r.add_area("second_figure")
