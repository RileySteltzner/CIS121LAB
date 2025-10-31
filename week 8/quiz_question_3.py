def count_duplicates(num1 = 0, num2 = 0, num3 = 0):
    if num1 == num2 and num2 == num3:
        return "3 numbers the same"
    elif num1 == num2 or num1 == num3:
        return "2 numbers are the same"
    elif num2 == num1 or num2 == num3:
        return "2 numbers are the same"
    elif num3 == num1 or num3 == num2:
        return "2 numbers are the same"
    elif num1 != num2 and num2 != num3:
        return "They are all unique"
print(count_duplicates(0))