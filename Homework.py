# ООП: наследование, инкапсуляция и полиморфизм


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}
        
      
class Reviewer(Mentor):
    def __init__(self):
        self.grades = {}
  

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
other_student = Student('Eli', 'Levy', 'your_gender')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
good_student = Student('Katrin', 'Johns', 'female')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Git']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
good_mentor = Mentor('Sam', 'Smith')
good_mentor.courses_attached += ['Python']

 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(other_student, 'Python', 5)
cool_mentor.rate_hw(other_student, 'Git', 7)
cool_mentor.rate_hw(other_student, 'Git', 10)
cool_mentor.rate_hw(other_student, 'Git', 9)
cool_mentor.rate_hw(good_student, 'Git', 8)
 
print(best_student.grades)
print(other_student.grades)
print(good_student.grades)