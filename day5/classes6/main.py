from day5.classes6.course import Course
from day5.classes6.student import Student

s1 = Student('Tim', 18, 5)
s2 = Student('John', 20, 3)
s3 = Student('Kenny', 21, 2)

course = Course('Media', 2)
print(course.add_student(s1))
print(course.add_student(s2))
print(course.add_student(s3))

print(course.get_average_grade())
