prices = {"flour": 2.50, "sugar": 1.80, "eggs": 3.00, "milk": 2.00, "butter": 2.75, "vanilla": 4.50, "chocolate": 5.00}
def total_cost(ingredients):
    total = 0
    for item in ingredients:
        if item in prices:
            total += prices[item]
    return total
print(total_cost(["flour", "sugar", "eggs", "butter"]))
