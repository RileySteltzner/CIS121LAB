#write a funtion that takes an int, adds two, then multiplies by 4
'''
def  my_func (integer):
    total = (integer + 2)*4
    return total 
print(my_func(5))
'''

#starting with value 10, add 2, then multiply by 4. 
#take the result and add 2 to it, then multiply by 4.

#write a function that returns the product of two arguments. 
'''
def product(num1, num2):
    total = num1 * num2
    return total
print(product(3,4))
'''

#in python, a list starts with [ and end with ]

#x = [] # this is a list with nothing in it 

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

#print the element of the lyst in position 1
'''
print(lyst[0])
'''
#print the portion of the lyst that is 3, false, and 4.5
'''
print(lyst[2:5])
'''
#lyst.append(elemet) will add the element to the end of the lyst.
print(lyst)
lyst.append(12)
print(lyst)
lyst.insert(2,12)
print(lyst)