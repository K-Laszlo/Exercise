class Course:

    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.student_list = []

    def add_student(self, student):
        student_added_to_course = False
        if len(self.student_list) < self.max_student:
            self.student_list.append(student)
            student_added_to_course = True
        return student_added_to_course

    def get_average_grade(self):
        value = 0
        for student in self.student_list:
            value = value + student.get_grade()
        return value / len(self.student_list)
