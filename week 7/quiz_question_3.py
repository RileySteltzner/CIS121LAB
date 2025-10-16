def find_two_unique(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    unique_nums = [num for num, count in counts.items() if count ==1]
    return unique_nums
print(find_two_unique([2,3,5,3,2,7]))