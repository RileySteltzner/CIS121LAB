larger = int(input("pick a number: "))
smaller = int(input("pick a number smaller than the last: "))

while larger > smaller:
    print(larger)
    larger = larger/2