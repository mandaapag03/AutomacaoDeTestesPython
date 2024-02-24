def calculate_tip(expenditure_amount):
    total_bill = expenditure_amount * 1.10
    tip_value = total_bill - expenditure_amount
    return {'total_bill' : round(total_bill, 2), 'tip_value' : round(tip_value ,2)}