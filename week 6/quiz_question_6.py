def find_factors(num):
    results = []
    for i in range(1,num+1):
        if num % i == 0:
            results.append(i)
    return results
user_num = int(input("Enter a number to find factors: "))
print (find_factors(user_num))