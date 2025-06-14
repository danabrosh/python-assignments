from circle_utils import calculate_area, calculate_circumference
from math import pi

def test_circle_area():
    assert calculate_area(1) == pi
    assert calculate_area(2) == 4 * pi
    assert calculate_area(0) == 0

def test_circle_circumference():
    assert calculate_circumference(1) == 2 * pi
    assert calculate_circumference(2) == 4 * pi
    assert calculate_circumference(0) == 0
