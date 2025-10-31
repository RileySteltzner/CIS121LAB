def list_of_multiples(num,length = 5):
    mutliples = []
    for i in range(1,length+1,):
        i = num * i
        mutliples.append(i)
    return mutliples
print(list_of_multiples(12,10))