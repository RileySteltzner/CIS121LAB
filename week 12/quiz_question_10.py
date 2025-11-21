class ShoppingCart:
    def __init__(self, items = {}):
        self.items = items
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
    def __add__(self, other):
        combined = ShoppingCart()
        for item, qty in self.items.items():
            combined.items[item] = qty
        for item, qty in other.items.items():
            if item in combined.items:
                combined.items[item] += qty
            else:
                combined.items[item] = qty
        return combined

    def __str__(self):
        return f"{self.items}"
        

p1 = ShoppingCart({"tea":1, "energy drink":3})
p2 = ShoppingCart({"energy drink":3, "hat": 1})
combined = p1 + p2
print(combined)

