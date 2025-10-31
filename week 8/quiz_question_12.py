def is_even(value):
    if value % 2 == 0:
        return value
def report_evens(lyst):
    even_nums = []
    for num in lyst:
        if is_even(num):
            even_nums.append(num)
    return even_nums
print(report_evens([4,3,12,16,8,9,25]))