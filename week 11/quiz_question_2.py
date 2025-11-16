class Ducks:
    def __init__(self, _name = "unknown", _color = "unknown"):
        self.name = _name
        self.color = _color
    def get_color(self):
        return self.color
    def set_color(self, value):
        self.color = value
    
    def speak(self):
        print (f'{self.name} says: Quack!')
    
    def __str__(self):
        return f'{self.name} is a duck that is {self.color}. '

class Pond:
    def __init__(self, _pond_name = "unknown"):
        self.pond_name = _pond_name
        self.ducks = []
    
    def add_duck(self, duck):
        self.ducks.append(duck)
    
    def ducks_quack(self):
        print (f'In {self.pond_name} pond, the ducks are quacking: ')
        for duck in self.ducks:
            print(f"{duck.name} who is {duck.color} is quacking!")
    def __str__(self):
        return f'In {self.pond_name} pond, there are 2 ducks named {len(self.ducks)}. '
    
pond1 = Pond("Sunny Lake")
duck1 = Ducks("Steve", "Black")
duck2 = Ducks("EJ", "Grey")
pond1.add_duck(duck1)
pond1.add_duck(duck2)
pond1.ducks_quack()
print (pond1)
    

    