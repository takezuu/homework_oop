import pytest
from src.Circle import Circle
from src.Square import Square
from src.Line import Line


@pytest.fixture()
def default_figure():
    circle = Circle(radius=7)
    yield circle
    del circle


def test_name(default_figure):
    assert default_figure.name == 'Circle'


def test_area(default_figure):
    assert default_figure.area == 153.86


def test_perimeter(default_figure):
    assert default_figure.perimeter == 43.96


def test_add_area(default_figure):
    square = Square(side=10)
    assert default_figure.add_area(square) == 253.86


def test_raise_add_area(default_figure):
    line = Line()
    assert default_figure.add_area(line) == 153.86
