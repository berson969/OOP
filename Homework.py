# ООП: наследование, инкапсуляция и полиморфизм


from tabnanny import check


def average(dict_grades):
    sm = 0
    ln = 0
    for values in dict_grades.values():
        sm += sum(values)
        ln += len(values)
    if ln == 0:
        return 'No grades'
    return round((sm / ln),1)
    
def average_in_course(list_person, course):
    sm = 0
    ln = 0
    for person in list_person:
        if course in person.grades.keys():
            sm += sum(person.grades[course]) 
            ln += len(person.grades[course])
    if ln == 0:
        return 'No grades'
    return round((sm / ln),1)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        list_students.append(self)
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 
        self.courses_in_progress.remove(course_name) 
        del self.grades[course_name] 

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def __average(self):
    #     sm = 0
    #     ln = 0
    #     for values in self.grades.values():
    #         sm += sum(values)
    #         ln += len(values)
    #     if ln == 0:
    #         return 'No grades'
    #     return round((sm / ln),1)

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}\nAvg grade of homeworks: {average(self.grades)}\nCourses in progress: {",".join(self.courses_in_progress)}\nFinished courses: {",".join(self.finished_courses)}\n\n'
 
    def __lt__(self, other):
        if not isinstance(other, type(self)) or type(average(self.grades)) != float or type(average(other.grades)) != float:
            return "It's wrong!"
        return average(self.grades) < average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        list_lecturer.append(self)

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}\nAvg grade of lectures: {average(self.grades)}\n\n'

    def __lt__(self, other):
        if not isinstance(other, type(self)) or type(average(self.grades)) != float or type(average(other.grades)) != float:
            return "It's wrong!"
        return average(self.grades) < average(other.grades)

   
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}\n\n'

    def __lt__(self, other):
        return "It's wrong!"


list_students = []
list_lecturer = []


#There are new students
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL']
other_student = Student('Eli', 'Levy', 'your_gender')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
good_student = Student('Ketlin', 'Johns', 'female')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Git']

#There are mentors 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['SQL']
cool_reviewer.courses_attached += ['Git']

good_lecturer = Lecturer('Sam', 'Smith')
good_lecturer.courses_attached += ['Python']

new_lecturer = Lecturer('Adam', 'Nolan')
new_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['SQL']

#Students Grades for homework 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'SQL', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 5)
cool_reviewer.rate_hw(other_student, 'Git', 7)
cool_reviewer.rate_hw(other_student, 'Git', 10)
cool_reviewer.rate_hw(other_student, 'Git', 9)
cool_reviewer.rate_hw(good_student, 'Git', 8)

#Students evaluate lectures
good_student.rate_lc(good_lecturer, 'Python', 2.75)
other_student.rate_lc(good_lecturer, 'Python', 10)
best_student.rate_lc(new_lecturer, 'Python', 10)
best_student.rate_lc(new_lecturer, 'SQL', 9)


print("\nGrades\n") 
print(best_student.grades)
print(other_student.grades)
print(good_student.grades)
print(good_lecturer.grades)


print("\n\nMentor's print\n")
print(cool_reviewer)
print(good_lecturer)
print(new_lecturer)


print("Student's print\n")
print(best_student)
print(other_student)
print(good_student)

print('The Compaisons\n')
print(new_lecturer > good_lecturer)
print(cool_reviewer < good_lecturer)
print(good_lecturer < cool_reviewer)
print(best_student < good_student)


# Average student's grade of course
print(f"\n Average student's grade of Python: {average_in_course(list_students, 'Python')}\n")

# Average  lecturer's grade of course
print(f"\n Average lecturer's grade of Python: {average_in_course(list_lecturer, 'Python')}\n")
print(f"\n Average lecturer's grade of SQL: {average_in_course(list_lecturer, 'Git')}\n")

# Student finished the course
best_student.add_courses('Python')
print(f"\n Average student's grade of Python: {average_in_course(list_students, 'Python')}\n")


check_student = Student('Garry', 'Potter', 'male')
check_student.courses_in_progress += ['Python']
# cool_reviewer.rate_hw(check_student, 'Python', 0)
# cool_reviewer.rate_hw(check_student, 'Python', 0)
print (cool_reviewer < check_student)
# print (check_student)
print (best_student.rate_lc(good_lecturer, 'Python', 10))