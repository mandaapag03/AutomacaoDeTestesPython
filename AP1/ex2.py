def add_discount(product_value): 
    new_value = product_value * (9/100)
    discount_value = product_value - new_value
    return {'discount_value': discount_value, 'new_value': new_value}