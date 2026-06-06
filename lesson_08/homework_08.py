# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, average_score):
        self.average_score = average_score

student_1 = Student('Mike', 'Johnson', 20, 5)
print(f'My name is {student_1.surname} {student_1.name}. I am {student_1.age} years old. My average_score is {student_1.average_score}.')

student_1.set_average_score(10)
print(f'My name is {student_1.surname} {student_1.name}. I am {student_1.age} years old. My average_score is {student_1.average_score}.')

