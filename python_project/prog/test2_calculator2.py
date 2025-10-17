# Unit test case to test square function in calculator2 app
# use pytest calculator2.py  to test the functionality
# It is better to break down the test into different categories to get a pattern of failures
from calculator2 import square
import pytest

def test__positive_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16


def test_positive_square():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero_square():
    assert square(0) == 0


def test_str_square():
    with pytest.raises(TypeError):
         square("cat")

