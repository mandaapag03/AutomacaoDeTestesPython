import pytest
from ex2 import add_discount

def test_input_calculate_1():
    assert add_discount(100) == {'discount_value': 91.00, 'new_value': 9.00}

def test_input_calculate_2():
    assert add_discount(1500) == {'discount_value': 1365.00, 'new_value': 135.00}

def test_input_calculate_3():
    assert add_discount(60000) == {'discount_value': 54600.00, 'new_value': 5400.00}