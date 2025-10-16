def ascending_order(num1,num2,num3):
    results = []
    if num1 < num2 and num2 < num3:
        results.append(num1)
        results.append(num2)
        results.append(num3)
    elif num2 < num1 and num1 < num3:
        results.append(num2)
        results.append(num1)
        results.append(num3)
    elif num3 < num1 and num2 <  num1:
        results.append(num3)
        results.append(num2)
        results.append(num1)
    elif num2 < num3 and num3 < num1:
        results.append(num2)
        results.append(num3)
        results.append(num1)
    elif num3 < num1 and num1 < num2:
        results.append(num3)
        results.append(num1)
        results.append(num2)
    return results
num1 = input("First Number: ")
num2 = input("Second Number: ")
num3 = input("Third Number: ")
print(ascending_order(num1,num2,num3))