def find_relation(name = " "):
    if name == "Darth Vader":
        return "Father"
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother in Law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "unknown"
print(find_relation())