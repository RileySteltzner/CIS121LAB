def num_copies(num1,num2,num3):
    if num1 == num2 and num2 == num3:
        return 'All numbers the same'
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return 'Two numbers are the same'
    elif num1 != num2 and num2 != num3 and num1 != num3:
        return 'None of the numbers are the same'
print(num_copies(3,3,3))