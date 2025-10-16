def total_donations(donations):
    total = 0
    for num in donations.values():
        total += num
    return total
donations = {"john": 100, "Sarah": 200, "Mike": 50}
print(total_donations(donations))