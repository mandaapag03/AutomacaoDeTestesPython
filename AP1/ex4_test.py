from ex4 import calculate_tip

def test_input_calculate_1():
    assert calculate_tip(75.00) == {'total_bill' : 82.50, 'tip_value' : 7.5}

def test_input_calculate_2():
    assert calculate_tip(125) == {'total_bill' : 137.50, 'tip_value' : 12.5}

def test_input_calculate_3():
    assert calculate_tip(350.87) == {'total_bill' : 385.96, 'tip_value' : 35.09}