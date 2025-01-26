def test_add_positive_numbers(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(10, 20) == 30


def test_add_negative_numbers(calc):
    assert calc.add(-1, -1) == -2
    assert calc.add(-5, -3) == -8


def test_add_mixed_numbers(calc):
    assert calc.add(-1, 1) == 0
    assert calc.add(-10, 5) == -5


def test_add_with_zero(calc):
    assert calc.add(0, 0) == 0
    assert calc.add(0, 5) == 5
    assert calc.add(5, 0) == 5


def test_add_floats(calc):
    assert calc.add(2.5, 3.1) == 5.6
    assert calc.add(-2.5, 2.5) == 0.0


def test_add_large_numbers(calc):
    assert calc.add(1_000_000, 2_000_000) == 3_000_000
    assert calc.add(-1_000_000, -2_000_000) == -3_000_000
