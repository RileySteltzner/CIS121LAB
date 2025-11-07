class Student:
    def __init__(self):
        self.name = "unknown"
        self.major = "unknown"
        self.gpa = 0
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_major(self):
        return self.major
    def set_major(self, student_major):
        self.major = student_major
    
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, student_gpa):
        self.gpa = student_gpa
    def new_gpa(self):
        new_gpa = self.gpa + 0.2
        if new_gpa <= 4.0:
            return new_gpa
        else:
            return "gpa too high"
        
    def __str__(self):
        return f"Hi I'm {self.name}. I am studying {self.major}. My GPA increased from {self.gpa} to {self.new_gpa()}"

student1 = Student()
student1.set_name ("Brittany")
student1.set_major ("Nursing")
student1.set_gpa (2.5)

print (student1)