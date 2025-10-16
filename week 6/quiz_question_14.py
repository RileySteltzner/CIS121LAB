def progress_days(miles):
    progress = 0
    for i in range(1, len(miles)):
        if miles[i] > miles[i - 1]:
            progress += 1
    return progress
user_miles = input("Enter list with [] of the miles you run each Sat. ")
print(progress_days(user_miles))