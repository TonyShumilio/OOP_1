class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"


    def av_rating(self):
        sum_raiting = 0
        len_raiting = 0
        for course in self.grades.values():
            sum_raiting += sum(course)
            len_raiting += len(course)
        average_rating = round(sum_raiting / len_raiting, 2)
        return average_rating


    def av_rating_for_course(self, course):
        sum_rating = 0
        lem_rating = 0
        for lesson in self.grades.keys():
            sum_rating += sum(self.grades[course])
            lem_rating += len(self.grades[course])
        average_rating = round(sum_rating / lem_rating, 2)
        return average_rating


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nГруппа: {self.group} \nСредняя оценка за домашние задания: {self.av_rating()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Error")
            return
        return self.av_rating() < other.av_rating()

#-------------------------------------------------

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#-------------------------------------------------

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def av_rating(self):
        sum_raiting = 0
        len_raiting = 0
        for course in self.grades.values():
            sum_raiting += sum(course)
            len_raiting += len(course)
        average_rating = round(sum_raiting / len_raiting, 2)
        return average_rating


    def av_rating_for_course(self, course):
        sum_rating = 0
        lem_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                lem_rating += len(self.grades[course])
        average_rating = round(sum_rating / lem_rating, 2)
        return average_rating


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_rating()}'
        return res


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error')
            return
        return self.av_rating() < other.av_rating()

#-------------------------------------------------

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

# -------------------------------------------------

student_1 = Student('James', 'Bond', '007')
student_1.courses_in_progress += ['PostgreSQL']
student_1.finished_courses += ['Git']

student_2 = Student('Above', 'Beyond', 'Group Therapy')
student_2.courses_in_progress += ['PostgreSQL']
student_2.finished_courses += ['Git']

# -------------------------------------------------

lecturer_1 = Lecturer('Dr', 'Who')
lecturer_1.courses_attached += ['PostgreSQL']

lecturer_2 = Lecturer('Alan', 'Wake')
lecturer_2.courses_attached += ['PostgreSQL']

# -------------------------------------------------

reviewer_1 = Reviewer('Big', 'Bro')
reviewer_1.courses_attached += ['PostgreSQL']

reviewer_2 = Reviewer('Dark', 'Tower')
reviewer_2.courses_attached += ['PostgreSQL']

# -------------------------------------------------

reviewer_1.rate_hw(student_1, 'PostgreSQL', 9)
reviewer_1.rate_hw(student_1, 'PostgreSQL', 8)
reviewer_1.rate_hw(student_1, 'PostgreSQL', 7)

reviewer_2.rate_hw(student_2, 'PostgreSQL', 9)
reviewer_2.rate_hw(student_2, 'PostgreSQL', 9)
reviewer_2.rate_hw(student_2, 'PostgreSQL', 10)

# -------------------------------------------------

student_1.rate_lw(lecturer_1, 'PostgreSQL', 10)
student_1.rate_lw(lecturer_1, 'PostgreSQL', 10)
student_1.rate_lw(lecturer_1, 'PostgreSQL', 9)

student_2.rate_lw(lecturer_2, 'PostgreSQL', 8)
student_2.rate_lw(lecturer_2, 'PostgreSQL', 7)
student_2.rate_lw(lecturer_2, 'PostgreSQL', 8)

# -------------------------------------------------

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]

# -------------------------------------------------

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for student in student_list:
        for course in student.grades:
            student_sum_rating = student.av_rating_for_course(course)
            sum_rating += student_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

# -------------------------------------------------

print('Средняя оценка за домашние задания всех студентов:')
print(average_rating_for_course('PostgreSQL', student_list))
print('Средняя оценка за лекции всех лекторов:')
print(average_rating_for_course('PostgreSQL', lecturer_list))

print('\n')
print(lecturer_1)
print('\n')
print(lecturer_2)

print('\n')
print(student_1)
print('\n')
print(student_2)

print('\n')
print(reviewer_1)
print('\n')
print(reviewer_2)



















