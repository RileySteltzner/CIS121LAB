class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    def set_price(self, value):
        self.price = value
    
    def show_description(self):
        print(f"The {self.name} is {self.price}")

    def __str__(self):
        return f'{self.name} is priced at {self.price}'

class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []
    
    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)
    
    def display_menu(self):
        print(f"Resturant: {self.restaurant_name}")
        print("menu:")
        for item in self.menu_items:
            print(f"{item.name} is {item.price}")
    
    def lunch_menu(self):
        print(f"Lunch menu for here is all items 2 dollars off")
        for item in self.menu_items:
            discounted_price = item.price - 2
            if discounted_price < 0:
                discounted_price = 0
            print(f'{item.name}: {discounted_price}')
    
    def __str__(self):
        return f"{self.restaurant_name} has {len(self.menu_items)} items"

restaurant1 = Restaurant("King")
item1 = MenuItem("Burger", 9.00)
item2 = MenuItem("Chicken", 10.00)
restaurant1.add_menu_item(item1)
restaurant1.add_menu_item(item2)
restaurant1.display_menu()
restaurant1.lunch_menu()
print(restaurant1)
        