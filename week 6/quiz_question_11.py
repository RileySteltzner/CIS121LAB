def add_lists(lyst1, lyst2):
    results = []
    for i in range(len(lyst1)):
        results.append(lyst1[i] + lyst2[i])
    return results
user_lyst1 = input()
user_lyst2 = input()
print(add_lists(user_lyst1, user_lyst2))