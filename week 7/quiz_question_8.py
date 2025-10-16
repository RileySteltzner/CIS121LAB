def find_youngest(people):
    min_age = min(people, key=people.get)
    return min_age
people = {"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}
print(find_youngest(people))