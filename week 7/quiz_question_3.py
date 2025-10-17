def find_two_unique(numbers):
    counts = {}
    unique_nums = []
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in counts:
        if counts[num]==1:
            unique_nums.append(num)
    return unique_nums
print(find_two_unique([2,3,5,3,2,7]))