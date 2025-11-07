class Recipe:
    def __init__(self):
        self.name = "unknown"
        self.cooking_time = 0

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    
    def is_quick_meal(self):
        if self.cooking_time < 30:
            return "True"
        else:
            return "False"
    
    def __str__(self):
        return f"{self.name} is a recipe that takes {self.cooking_time}. Is it a quick meal: {self.is_quick_meal()}"
    
recipe1 = Recipe()
recipe1.set_name("Pasta")
recipe1.set_cooking_time(45)

print (recipe1)
