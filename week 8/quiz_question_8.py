def descending_order(num1,num2 = 15,num3 =5):
    lyst = []

    if num1 > num2 and num2 > num3:
        lyst.append(num1)
        lyst.append(num2)
        lyst.append(num3)
    elif num3 > num2 and num2 > num1:
        lyst.append(num3)
        lyst.append(num2)
        lyst.append(num1)
    elif num1 > num3 and num3 > num2:
        lyst.append(num1)
        lyst.append(num3)
        lyst.append(num2)
    elif num3 > num1 and num1 > num2:
        lyst.append(num3)
        lyst.append(num1)
        lyst.append(num2)
    elif num2 > num1 and num1 > num3:
        lyst.append(num2)
        lyst.append(num1)
        lyst.append(num3)
    elif num2 > num3 and num3 > num1:
        lyst.append(num2)
        lyst.append(num3)
        lyst.append(num1)
    return lyst
print(descending_order(2,3,1))