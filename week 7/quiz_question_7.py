def min_grade(exams):
    min_course = min(exams, key=exams.get)
    return min_course
exams = {"math": 85, "History": 78, "Biology": 92, "English": 74}
print(min_grade(exams))
