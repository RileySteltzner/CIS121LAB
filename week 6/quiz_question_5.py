def hailstone_seq(n):
    print(n, end = " ")
    results = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            results.append(n)
        else:
            n = (3 * n) + 1
            results.append(n)
    return results
user_n = int(input("Enter a starting number: "))
print (hailstone_seq(user_n))