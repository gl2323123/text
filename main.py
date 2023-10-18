class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_grades = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_grades}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name: object, surname: object) -> object:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_grades = sum(map(sum, self.grades.values())) / grades_count
        result= f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за домашнее задание: {self.average_grades}\n'
        return result



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
        return (f'Имя:{self.name} \nФамилия:{self.surname}')

some_lecturer_1 = Lecturer('Ivan', 'Ivanov')
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Petr', 'Petrov')
some_lecturer_2.courses_attached += ['Java']

some_lecturer_3 = Lecturer('Semen', 'Zarev')
some_lecturer_3.courses_attached += ['Python']

some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Java']

some_reviewer_2 = Reviewer('Ostap', 'Bender')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Java']

student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Java', 'Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progress += ['Python','Git']
student_3.finished_courses += ['Введение в программирование']

# Оценки за дз
some_reviewer_1.rate_hw(student_1, 'Python', 8)
some_reviewer_1.rate_hw(student_1, 'Python', 9)
some_reviewer_1.rate_hw(student_1, 'Python', 10)

some_reviewer_2.rate_hw(student_2, 'Java', 8)
some_reviewer_2.rate_hw(student_2, 'Java', 7)
some_reviewer_2.rate_hw(student_2, 'Java', 9)

some_reviewer_2.rate_hw(student_3, 'Python', 8)
some_reviewer_2.rate_hw(student_3, 'Python', 7)
some_reviewer_2.rate_hw(student_3, 'Python', 9)
some_reviewer_2.rate_hw(student_3, 'Python', 8)
some_reviewer_2.rate_hw(student_3, 'Python', 7)
some_reviewer_2.rate_hw(student_3, 'Python', 9)

# Оценки за лекции
student_1.rate_hw(some_lecturer_1, 'Python', 10)
student_1.rate_hw(some_lecturer_1, 'Python', 10)
student_1.rate_hw(some_lecturer_1, 'Python', 10)

student_1.rate_hw(some_lecturer_2, 'Python', 5)
student_1.rate_hw(some_lecturer_2, 'Python', 7)
student_1.rate_hw(some_lecturer_2, 'Python', 8)

student_1.rate_hw(some_lecturer_1, 'Python', 7)
student_1.rate_hw(some_lecturer_1, 'Python', 8)
student_1.rate_hw(some_lecturer_1, 'Python', 9)

student_2.rate_hw(some_lecturer_2, 'Java', 10)
student_2.rate_hw(some_lecturer_2, 'Java', 8)
student_2.rate_hw(some_lecturer_2, 'Java', 9)

student_3.rate_hw(some_lecturer_3, 'Python', 5)
student_3.rate_hw(some_lecturer_3, 'Python', 6)
student_3.rate_hw(some_lecturer_3, 'Python', 7)

print(student_3)

print(some_lecturer_2)

print(some_reviewer_1)