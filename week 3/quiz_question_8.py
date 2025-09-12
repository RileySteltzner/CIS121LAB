n1 = input("Pick a number: ")
n2 = input("pick another number: ")
n3 = input("Pick another number: ")

if (n1 > n2) and (n1 > n3):
    print(f'the largest number is {n1} .')
elif (n2 > n1) and (n2 > n3):
    print(f'the largest number is {n2} .')
else:
    if (n3 > n1) and (n3 > n2):
        print(f'the largest number is {n3} ')
