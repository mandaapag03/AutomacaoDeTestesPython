from ex3 import apply_discount

def test_input_calculate_1():
    assert apply_discount(500.00, 50.00) == 450.00

def test_input_calculate_2():
    assert apply_discount(10500.00, 500.00) == 10000.00

def test_input_calculate_3():
    assert apply_discount(90.00, 0.80) == 89.20