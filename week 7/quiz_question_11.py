def count_repetitions(elements):
    count = {}
    for item in elements:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
print(count_repetitions(['cat', 'dog', 'cat', 'cow', 'cow', 'cow']))