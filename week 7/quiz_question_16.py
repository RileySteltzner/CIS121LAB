calories = {"apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102}

def total_calories(fruit_list):
    total = 0
    for fruit in fruit_list:
        if fruit in calories:
            total += calories[fruit]
    return total
print(total_calories(["apple", "banana", "orange"]))