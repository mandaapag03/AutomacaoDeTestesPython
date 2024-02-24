import math

def calculate_teacher_salary(value_per_hour, num_classes, inss_percentual):
    gross_wage = value_per_hour * num_classes
    net_wage = gross_wage - (gross_wage * (inss_percentual/100))
    return round(net_wage, 2) 
