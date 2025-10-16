def get_name(techid_dict):
    list_of_names = []
    for key in techid_dict:
        name = techid_dict[key]
        list_of_names.append(name)
    return list_of_names
dictionary = {}
print(get_name(dictionary))