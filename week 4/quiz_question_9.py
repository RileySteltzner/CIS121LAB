'''
width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
pattern = input("Enter a pattern: ")

row = 0 
while row < height:
    column = 0 
    while column < width:
        print(pattern, end="")
        column += 1
    print()
    row += 1
'''

height = int(input())
pattern = input()
row = 0 
while row <= height:
    print(pattern * row)
    row += 1 
print()

