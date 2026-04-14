# ============================================================
# pytest - Unit Tests: Taschenrechner
# Autor: Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM
# Framework: pytest
# Zweck: Grundlegende Rechenoperationen testen
# ============================================================

import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt.")
        return a / b


@pytest.fixture
def calc():
    return Calculator()


class TestCalculatorPositive:

    def test_addition(self, calc):
        assert calc.add(2, 3) == 5

    def test_addition_negative_numbers(self, calc):
        assert calc.add(-4, -6) == -10

    def test_subtraction(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_multiply(self, calc):
        assert calc.multiply(3, 7) == 21

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_divide_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5


class TestCalculatorNegative:

    def test_divide_by_zero_raises_exception(self, calc):
        with pytest.raises(ValueError, match="Division durch Null"):
            calc.divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected

# Terminal: pytest test_calculator.py -v
