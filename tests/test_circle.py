import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestCircle:
    @pytest.mark.parametrize('radius, perimeter, area',
                             [
                                 (1, 6.28, 3.14),
                                 (10, 62.83, 314.16),
                                 (50, 314.16, 7853.98),
                             ])
    def test_circle(self, radius, perimeter, area):
        """
        Проверка вычисления площади и периметра для фигуры "Круг"
        """
        r = Circle(radius)
        assert r.name == 'Circle'
        assert r.calculate_perimeter() == perimeter
        assert r.calculate_area() == area

    @pytest.mark.parametrize('radius',
                             [
                                 -1, 0,
                             ])
    def test_circle_negative(self, radius):
        """
        Проверка вывода ошибки создания фигуры "Круг"
        """
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize('radius, radius1, result',
                             [
                                 (10, 50, 8168.14),
                             ])
    def test_add_area_circle(self, radius, radius1, result):
        """
        Проверка вычисления суммы площадей для фигуры "Круг"
        """
        c1 = Circle(radius)
        c2 = Circle(radius1)
        assert c1.add_area(c2) == result

    @pytest.mark.parametrize('radius, side_a1, side_b1, result',
                             [
                                 (10, 2, 10, 334.16),
                             ])
    def test_add_area_circle_w_rectangle(self, radius, side_a1, side_b1, result):
        """
        Проверка вычисления суммы площадей для фигур "Круг" и "Прямоугольник"
        """
        c = Circle(radius)
        r = Rectangle(side_a1, side_b1)
        assert c.add_area(r) == result

    @pytest.mark.parametrize('radius, side_a1, result',
                             [
                                 (10, 10, 414.16),
                             ])
    def test_add_area_circle_w_square(self, radius, side_a1, result):
        """
        Проверка вычисления суммы площадей для фигур "Круг" и "Квадрат"
        """
        c = Circle(radius)
        s = Square(side_a1)
        assert c.add_area(s) == result

    @pytest.mark.parametrize('radius, side_a1, side_b1, side_c1, result',
                             [
                                 (10, 10, 15, 20, 386.78),
                             ])
    def test_add_area_circle_w_triangle(self, radius, side_a1, side_b1, side_c1, result):
        """
        Проверка вычисления суммы площадей для фигур "Круг" и "Треугольник"
        """
        c = Circle(radius)
        t = Triangle(side_a1, side_b1, side_c1)
        assert c.add_area(t) == result

    @pytest.mark.parametrize('radius',
                             [
                                 10,
                             ])
    def test_add_area_circle_negative(self, radius):
        """
        Проверка вывода ошибки вычисления суммы площадей для фигуры "Круг"
        """
        c = Circle(radius)
        with pytest.raises(ValueError):
            c.add_area("second_figure")
