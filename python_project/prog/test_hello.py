from hello import hello

def test_default_hello():
    assert hello()  == "hello, world"


def test_argument_hello():
    for name in ["A", "B", "C"]:
        assert hello(name) == f"hello, {name}"
