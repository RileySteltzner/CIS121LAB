class Star:
    def __int__(self, _name, ):
        self.name = _name
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def __str__(self):
        msg = " "
        msg = f'I am the {self.name}! Leader of the stars round earth'
        return msg
    
sun = Star("Sun")
print(sun.get_name())