'''
age = int(input("enter your age: "))

if age < 3: 
    print('Price = Free')

else:
    if age < 18: 
        print('Price = 10')
    else:  
        if age > 65: 
            print('Price = 15')
        else: 
            print('Price = 20')
            '''
age = int(input("enter your age: "))
status = '...'
if age < 3: 
    print('Price = Free')
elif age < 18: 
    print('Price = 10')
elif age > 65: 
    print('price = 15')
else: 
    if status == 'Military':
        print('price = 15')
    elif status == 'Student':
        print('Price = 16')
    else:
        print('Price = 20')
    




