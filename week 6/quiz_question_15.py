def lag_days(miles):
    lag = 0
    for i in range(1,len(miles)):
        if miles[i] < miles[i - 1]:
            lag += 1
    return lag
user_miles = input("Enter numbers within [#, #, #, #]")
print(lag_days(user_miles))