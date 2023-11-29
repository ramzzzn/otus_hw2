import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                             [
                                 (1, 1, 1, 3, 0.43),
                                 (10, 15, 20, 45, 72.62),
                                 (0.5, 0.5, 0.5, 1.5, 0.11),
                             ], ids=["min", "int", "float"])
    def test_triangle(self, side_a, side_b, side_c, perimeter, area):
        """
        Проверка вычисления площади и периметра для фигуры "Треугольник"
        """
        r = Triangle(side_a, side_b, side_c)
        assert r.name == 'Triangle'
        assert r.calculate_perimeter() == perimeter
        assert r.calculate_area() == area

    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [
                                 pytest.param(
                                     0, 0, 0, id="null"),
                                 pytest.param(
                                     0, 1, 1, id="null"),
                                 pytest.param(
                                     1, 0, 1, id="null"),
                                 pytest.param(
                                     1, 1, 0, id="null"),
                                 pytest.param(
                                     -1, -2, -3, id="negative"),
                                 pytest.param(
                                     1, -2, -3, id="negative"),
                                 pytest.param(
                                     -1, 2, -3, id="negative"),
                                 pytest.param(
                                     -1, -2, 3, id="negative"),
                                 pytest.param(
                                     10, 5, 5, id="incorrect"),
                                 pytest.param(
                                     5, 10, 5, id="incorrect"),
                                 pytest.param(
                                     5, 5, 10, id="incorrect"),
                                 pytest.param(
                                     20, 5, 5, id="incorrect"),
                                 pytest.param(
                                     5, 20, 5, id="incorrect"),
                                 pytest.param(
                                     5, 5, 20, id="incorrect")
                             ]
                             )
    def test_triangle_negative(self, side_a, side_b, side_c):
        """
        Проверка вывода ошибки создания фигуры "Треугольник"
        """
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize('side_a, side_b, side_c, side_a1, side_b1, side_c1, result',
                             [
                                 (10, 15, 20, 50, 50, 50, 1155.15),
                             ], ids=['add_area_triangle_w_triangle'])
    def test_add_area_triangle(self, side_a, side_b, side_c, side_a1, side_b1, side_c1, result):
        """
        Проверка вычисления суммы площадей для фигуры "Треугольник"
        """
        t1 = Triangle(side_a, side_b, side_c)
        t2 = Triangle(side_a1, side_b1, side_c1)
        assert t1.add_area(t2) == result

    @pytest.mark.parametrize('side_a, side_b, side_c, side_a1, side_b1, result',
                             [
                                 (10, 15, 20, 10, 2, 92.62),
                             ], ids=['add_area_triangle_w_rectangle'])
    def test_add_area_triangle_w_rectangle(self, side_a, side_b, side_c, side_a1, side_b1, result):
        """
        Проверка вычисления суммы площадей для фигур "Треугольник" и "Прямоугольник"
        """
        t = Triangle(side_a, side_b, side_c)
        r = Rectangle(side_a1, side_b1)
        assert r.add_area(t) == result

    @pytest.mark.parametrize('side_a, side_b, side_c, side_a1, result',
                             [
                                 (10, 15, 20, 10, 172.62),
                             ], ids=['add_area_triangle_w_square'])
    def test_add_area_triangle_w_square(self, side_a, side_b, side_c, side_a1, result):
        """
        Проверка вычисления суммы площадей для фигур "Треугольник" и "Квадрат"
        """
        t = Triangle(side_a, side_b, side_c)
        s = Square(side_a)
        assert t.add_area(s) == result

    @pytest.mark.parametrize('side_a, side_b, side_c, radius, result',
                             [
                                 (10, 15, 20, 10, 386.78),
                             ], ids=['add_area_triangle_w_circle'])
    def test_add_area_triangle_w_circle(self, side_a, side_b, side_c, radius, result):
        """
        Проверка вычисления суммы площадей для фигур "Треугольник" и "Круг"
        """
        t = Triangle(side_a, side_b, side_c)
        c = Circle(radius)
        assert t.add_area(c) == result

    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [
                                 (10, 15, 20),
                             ], ids=['add_area_triangle_negative'])
    def test_add_area_triangle_negative(self, side_a, side_b, side_c):
        """
        Проверка вывода ошибки вычисления суммы площадей для фигуры "Треугольник"
        """
        t = Triangle(side_a, side_b, side_c)
        with pytest.raises(ValueError):
            t.add_area("second_figure")
