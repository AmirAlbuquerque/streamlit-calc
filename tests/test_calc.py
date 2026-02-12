from src.backend.calc import add

def test_add_integers():
    assert add(2, 3) == 5.0

def test_add_floats():
    assert add(0.1, 0.2) == 0.30000000000000004  # comportamento float padrão
