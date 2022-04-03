import pytest
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Line import Line


@pytest.fixture()
def default_figure():
    rectangle = Rectangle(side1=10, side2=17)
    yield rectangle
    del rectangle


def test_name(default_figure):
    assert default_figure.name == 'Rectangle'


def test_area(default_figure):
    assert default_figure.area == 170


def test_perimeter(default_figure):
    assert default_figure.perimeter == 54


def test_add_area(default_figure):
    triangle = Triangle(side1=10, side2=6, side3=8)
    assert default_figure.add_area(triangle) == 194


def test_raise_add_area(default_figure):
    line = Line()
    assert default_figure.add_area(line) == 170
