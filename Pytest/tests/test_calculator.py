import pytest
from src import calculator

def test_add():
    assert calculator.add(8,12) == 20
    
def test_add_wrong():
    assert calculator.add_wrong(8,12) == 20

def test_substract():
    assert calculator.substract(12,8) == 4
    
def test_multiply():
    assert calculator.multiply(8,12) == 96
    
def test_multiply_wrong():
    assert calculator.multiply_wrong(8,12) == 96
    
def test_divide():
    assert calculator.divide(12,4) == 3