standards = int(input("How many standards did you get this semester? "))

if standards == 57:
    print("A+")
elif standards > 53 or standards == 5:
    print("A ")
elif standards > 51 or standards == 51:
    print("A-")
elif standards > 49 or standards == 49:
    print("B+")
elif standards > 47 or standards == 47:
    print("B")
elif (standards > 45) or (standards == 45):
    print ("B-")
elif (standards > 43) or (standards == 43):
    print("C+")
elif (standards > 40) or (standards == 40):
    print("C")
elif ( standards >= 35 and standards < 40):
    print("D")
else: 
    print("F")

