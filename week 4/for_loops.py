#print numbers 1..10
'''
for number in range(1,11):
    print (number, end="")
'''

#print all even numbers between 1..10
'''
for number in range(1,11):
    if number % 2 == 0:
        print(number)
'''

#print all of the odd number between 5 and some 
#user given value
'''
user_value = int(input("Enter a number: "))

for num in range(5,user_value+1):
    if num % 2 ==1:
        print(num, end="")
'''
#find the sum of user entered values until 
#the user types 'q'
'''
total = 0

while True:
    user_values = input("Enter a number or 'q' to quit: ")

    if user_values == 'q':
        break
    total += int(user_values)
print(total)
'''




