import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestSquare:
    @pytest.mark.parametrize('side_a, perimeter, area',
                             [
                                 (1, 4, 1),
                                 (10, 40, 100),
                                 (50, 200, 2500)
                             ])
    def test_square(self, side_a, perimeter, area):
        """
        Проверка вычисления площади и периметра для фигуры "Квадрат"
        """
        r = Square(side_a)
        assert r.name == 'Square'
        assert r.calculate_perimeter() == perimeter
        assert r.calculate_area() == area

    @pytest.mark.parametrize('side_a',
                             [
                                 -5, 0
                             ])
    def test_square_negative(self, side_a):
        """
        Проверка вывода ошибки создания фигуры "Квадрат"
        """
        with pytest.raises(ValueError):
            Square(side_a)

    @pytest.mark.parametrize('side_a, side_a1, result',
                             [
                                 (10, 50, 2600),
                             ])
    def test_add_area_square(self, side_a, side_a1, result):
        """
        Проверка вычисления суммы площадей для фигуры "Квадрат"
        """
        s1 = Square(side_a)
        s2 = Square(side_a1)
        assert s1.add_area(s2) == result

    @pytest.mark.parametrize('side_a, side_a1, side_b1, result',
                             [
                                 (10, 2, 10, 120),
                             ])
    def test_add_area_square_w_rectangle(self, side_a, side_a1, side_b1, result):
        """
        Проверка вычисления суммы площадей для фигур "Квадрат" и "Прямоугольник"
        """
        s = Square(side_a)
        r = Rectangle(side_a1, side_b1)
        assert s.add_area(r) == result

    @pytest.mark.parametrize('side_a, radius, result',
                             [
                                 (10, 10, 414.16),
                             ])
    def test_add_area_square_w_circle(self, side_a, radius, result):
        """
        Проверка вычисления суммы площадей для фигур "Квадрат" и "Круг"
        """
        s = Square(side_a)
        c = Circle(radius)
        assert s.add_area(c) == result

    @pytest.mark.parametrize('side_a, side_a1, side_b1, side_c1, result',
                             [
                                 (10, 10, 15, 20, 172.62),
                             ])
    def test_add_area_square_w_triangle(self, side_a, side_a1, side_b1, side_c1, result):
        """
        Проверка вычисления суммы площадей для фигур "Квадрат" и "Треугольник"
        """
        s = Square(side_a)
        t = Triangle(side_a1, side_b1, side_c1)
        assert s.add_area(t) == result

    @pytest.mark.parametrize('side_a',
                             [
                                 10,
                             ])
    def test_add_area_square_negative(self, side_a):
        """
        Проверка вывода ошибки вычисления суммы площадей для фигуры "Квадрат"
        """
        s = Square(side_a)
        with pytest.raises(ValueError):
            s.add_area("second_figure")
