class Time:
    def __init__(self, hours, minutes):
        self.h = hours
        self.m = minutes
    def __add__(self, other):
        new_hours = self.h + other.h
        new_minutes = self.m + other.m
        if new_minutes > 60:
            new_hours += new_minutes // 60
            new_minutes = new_minutes % 60
            
        
        return Time(new_hours, new_minutes)
    def __str__(self):
        return f"{self.h} Hours {self.m} minutes"
    

time1 = Time(7,32)
time2 = Time(7,48)
time3 = time1 + time2
print(time1)
print(time2)
print(time3)