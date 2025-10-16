def find_oldest(age_dict):
    oldest_person = ""
    max_age = -1
    for curr_name in age_dict:
        curr_age = age_dict[curr_name]
        if curr_age > max_age:
            max_age = curr_age
            oldest_person = curr_name
    return oldest_person