class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    def set_price(self, value):
        self.price = value

    def display_info(self):
        print(f"{self.name} cost ${self.price}")
    
    def __str__(self):
        return f'The item {self.name} is ${self.price}. '

class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product
            print(total)
    
    def __str__(self):
        return f'This shopping cart with customer {self.customer_id} and has {len(self.procuts)} items'
    

shoppingcart1 = ShoppingCart("1234")
product1 = Product("Cheese", 4.50)
product2 = Product("Milk", 7.00)
shoppingcart1.add_product(product1)
shoppingcart1.add_product(product2)
shoppingcart1.display
print(shoppingcart1)
