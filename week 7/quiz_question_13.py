def total_sales(sales):
    total = 0
    for units in sales.values():
        total += units
    return total
sales = {"laptop": 5, "Phone": 10, "tablet": 3}
print(total_sales(sales))
