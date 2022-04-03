import pytest
from src.Circle import Circle
from src.Triangle import Triangle
from src.Line import Line


@pytest.fixture()
def default_figure():
    triangle = Triangle(side1=7, side2=10, side3=5)
    yield triangle
    del triangle


def test_name(default_figure):
    assert default_figure.name == 'Triangle'


def test_area(default_figure):
    assert default_figure.area == 16.25


def test_perimeter(default_figure):
    assert default_figure.perimeter == 22


def test_add_area(default_figure):
    circle = Circle(radius=10)
    assert default_figure.add_area(circle) == 330.25


def test_raise_add_area(default_figure):
    line = Line()
    assert default_figure.add_area(line) == 16.25
