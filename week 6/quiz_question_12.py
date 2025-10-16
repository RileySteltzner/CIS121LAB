def largest_even(lyst):
    largest = -1
    for i in lyst:
        if i % 2 == 0:
            if i > largest:
                largest = i
    return largest 
print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))