def get_indices(list,item):
    results = []
    for i in range(len(list)):
        if list[i] == item:
            results.append(i)
    return results
print (get_indices([1,5,5,2,7], 7))