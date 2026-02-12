from src.backend.calc import add, multiply, division

def test_add_integers():
    assert add(2, 3) == 5.0

def test_add_floats():
    assert add(0.1, 0.2) == 0.30000000000000004

def test_multiply_integers():
    assert multiply(2, 3) == 6.0

def test_multiply_floats():
    assert multiply(0.5, 0.2) == 0.1

def test_division_floats():
    assert division(4.0, 2.0) == 2.00000000000000004
