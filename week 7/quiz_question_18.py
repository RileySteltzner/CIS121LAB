def majority_elements(nums):
    most_often = None
    count = 0 
    for num in nums:
        if count == 0:
            most_often = num
        count += (1 if num == most_often else -1)
    return most_often
print(majority_elements([2,2,1,1,1,2,2]))
