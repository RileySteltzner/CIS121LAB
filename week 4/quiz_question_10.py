largest = -1

while True:
    num = int(input("Enter an integer or a negative integer to stop: "))
    if num < 0:
        break 
    if num % 2 == 0 and num > largest:
        largest = num
print ("largest even number is:", largest)