import pytest
from ex1 import calculate_teacher_salary

def test_input_calculate_1():
    assert calculate_teacher_salary(6.25, 160, 1.3) == 987.00

def test_input_calculate_2():
    assert calculate_teacher_salary(20.5, 240, 1.7) == 4836.36

def test_input_calculate_3():
    assert calculate_teacher_salary(13.9, 200, 6.48) == 2599.86