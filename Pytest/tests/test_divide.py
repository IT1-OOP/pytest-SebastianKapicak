import pytest
from src import calculator

def test_divide():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_divide_2():
    with pytest.raises(NameError):
        calculator.divide(5, 0)

@pytest.mark.parametrize(
    "a,b, expected_exception, expected_msg",
    [
        (0,5, ValueError, "Cannot take log of non-positive number!"),
        (-2,5, ValueError, "Cannot take log of non-positive number!"),
        (9,-2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5,1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a,b, expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        calculator.log(a,b)
    assert str(exc.value) == expected_msg