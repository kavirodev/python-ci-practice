
from main import add, multiply, is_even


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 3) == 12


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
