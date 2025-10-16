def find_unique(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1 
        else:
            count[num] = 1
    for num in count:
        if count[num] == 1:
            return num
