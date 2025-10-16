n1 = int(input("Pick a number: "))
n2 = int(input("Pick another number: "))
n3 = int(input("Pick another number: "))

if n1 > n2:
    n1 , n2 = n2 , n1
if n1 > n3:
    n1 , n3 = n3 , n1
if n2 > n3:
    n2 , n3 = n3 , n2
    print(n1, n2, n3)