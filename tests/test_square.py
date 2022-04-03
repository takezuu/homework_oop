import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Line import Line


@pytest.fixture()
def default_figure():
    square = Square(side=10)
    yield square
    del square


def test_name(default_figure):
    assert default_figure.name == 'Square'


def test_area(default_figure):
    assert default_figure.area == 100


def test_perimeter(default_figure):
    assert default_figure.perimeter == 40


def test_add_area(default_figure):
    rectangle = Rectangle(side1=10, side2=5)
    assert default_figure.add_area(rectangle) == 150


def test_raise_add_area(default_figure):
    line = Line()
    assert default_figure.add_area(line) == 150
