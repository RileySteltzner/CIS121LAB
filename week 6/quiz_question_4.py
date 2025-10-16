def odd_numbers(smaller_num, larger_num):
    results =[]
    for n in range(smaller_num,larger_num+1):
        if n % 2 != 0:
            results.append(n)
    return results
smaller = int(input("Enter a small number: "))
larger = int(input("Enter a large number: "))
print(odd_numbers(smaller,larger))