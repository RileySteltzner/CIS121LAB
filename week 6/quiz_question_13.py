def largest_odd(lyst):
    largest = -1
    for i in lyst:
        if i % 2 != 0:
            if i > largest:
                largest = i
    return largest 
print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))