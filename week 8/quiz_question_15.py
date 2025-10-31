def is_negative(num):
    if num < 0:
        return num
def is_odd(num):
    if num % 2 != 0:
        return num
def report_negative_odd(lyst):
    result_lyst = []
    for num in lyst:
        if is_negative(num) and is_odd(num):
            result_lyst.append(num)
    return result_lyst
print(report_negative_odd([100,-57,12,1,-36,-15]))
