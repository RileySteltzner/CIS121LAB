width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
pattern = input("Enter a pattern: ")

row = 1 
while row <= height:
    column = 1 
    while column <= width:
        print(pattern, end="")
        column += 1
    print()
    row += 1