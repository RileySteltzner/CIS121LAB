def get_indices(lyst,value = 0):
    num_indices = []
    for i in range(len(lyst)):
        if lyst[i] == value:
            num_indices.append(i)
    return num_indices
print(get_indices([1,0,5,0,7]))