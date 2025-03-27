import pytest

from projects.basics.calculator import Calculator

class TestCalculator:

    @pytest.fixture
    def calculator(self):
        calc = Calculator()
        return calc

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -1, -2),
        (0, 5, 5)
    ])
    def test_add(self, calculator, a, b, expected):
        assert calculator.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 2, 4),
        (0, 4, -4),
        (3, 4, -1)
    ])
    def test_substract(self, calculator, a, b, expected):
        assert calculator.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 5, 20),
        (1, 5, 5),
        (3, 6, 18)
    ])
    def test_multiply(self, calculator, a, b, expected):
        assert calculator.multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2),
        (4, 4, 1),
        (8, 4, 2)
    ])
    def test_divide(self, calculator, a, b, expected):
        assert calculator.divide(a, b) == expected

    def test_zero_division(self, calculator):
        with pytest.raises(ZeroDivisionError) as error:
            calculator.divide(10, 0)
        assert error.value.args[0] == "Cannot divide by zero"
