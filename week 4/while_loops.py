'''
number = 1
while number <= 10: 
    print(number)
    number += 1
'''
#print even numbers between 1-10
'''
number = 2
while number <= 10:
    print(number)
    number += 2 
'''
'''
number = 1 
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1
'''
#print all the odd numbers between 5 and
#some number given by the user
'''
start_number = 5
num = int(input(" enter a number greater than 5: "))

while start_number <= num:
    if start_number % 2 ==1:
        print(start_number)
    start_number += 1
    '''

#print all even numbers that are not devisible by 3
'''
number = 1

while number < 50:
    if number % 2 == 0:
        if number % 3 ==0:
            #do nothing and 
            #skip rest of code
            continue
        print(number)
    number += 1 
'''