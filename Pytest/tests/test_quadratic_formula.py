from src import calculator
import pytest


def test_quadratic_formula():
    assert calculator.solve_quadratic_formula(1, -5, 4) == (4.0, 1.0)
    assert calculator.solve_quadratic_formula(1, 3, -10) == (2.0, -5.0)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -2, 1, (1.0, 1.0)),  
        (1, -5, 6, (3.0, 2.0)),  
        (1, 1, -6, (2.0, -3.0)),  
    ]
)
def test_solve_quadratic_formula(a, b, c, expected):
    assert calculator.solve_quadratic_formula(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected_exception, expected_msg",
    [
        ("b", -2, 3, TypeError, "All coefficients must be of type float or int!"),  
        (0, -3, 2, ValueError, "Cannot solve quadratic formula with a = 0!"),  
        (1, 5, 3, ValueError, "I don't like when b = 5!"),  
        (1, 3, 6, ValueError, "Cannot solve quadratic formula with negative discriminant!"),  
    ],
)
def test_exception(a, b, c, expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        calculator.solve_quadratic_formula(a, b, c)
    assert str(exc.value) == expected_msg