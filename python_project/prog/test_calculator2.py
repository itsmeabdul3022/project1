# Unit test case to test square function in calculator2 app
# use pytest calculator2.py  to test the functionality
from calculator2 import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

