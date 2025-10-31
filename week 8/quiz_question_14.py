def is_two_digit_number(value):
    if value in range(-99,-10):
        return value
    elif value in range (10,99):
        return value
def report_two_digit_numbers(lyst):
    numbers = []
    for num in lyst:
        if is_two_digit_number(num):
            numbers.append(num)
    return numbers
print(report_two_digit_numbers([121,36,-19,-6,0,21]))