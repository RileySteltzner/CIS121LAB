class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_major(self):
        return self.major
    def set_major(self, new_major):
        self.major = new_major
    
    def __str__(self):
        return f' {self.name} is majoring in {self.major}'

class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.student : Student=[]
    
    def get_number(self):
        return self.course_number
    def set_number(self, new_course_number):
        self.course_number = new_course_number
    
    def add_student(self, student: Student):
        self.student.append(student)
    
    def show_student_enrollment(self):
        for student in self.student:
            print(student)
   
course = Course("Intro to Programming", 121)
student1 = Student("John", "Computer Science")
student2 = Student("Matt", "Computer Engineering")
course.add_student(student1)
course.add_student(student2)
course.show_student_enrollment()

