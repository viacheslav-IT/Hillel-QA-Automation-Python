import random
from pony.orm import Database, Required, Set, db_session, select

db = Database()


# Створення моделі даних
class Course(db.Entity):
    name = Required(str)
    students = Set('Student')

class Student(db.Entity):
    name = Required(str)
    courses = Set(Course)

db.bind(provider='sqlite', filename='students_system.db', create_db=True)
db.generate_mapping(create_tables=True)


# Базові функції
@db_session
def init_seed_data():
    if select(c for c in Course).count() > 0:
        return

    # Створюємо 5 курсів
    course_names = ["Python Basics", "Databases SQL", "Web Development", "DevOps Intro", "Data Science"]
    courses = [Course(name=name) for name in course_names]

    # Створюємо 20 студентів і записуємо їх на випадкові курси
    student_names = [
        "Олексій", "Марія", "Іван", "Олена", "Дмитро",
        "Анна", "Сергій", "Юлія", "Максим", "Ольга",
        "Артем", "Наталія", "Андрій", "Вікторія", "Павло",
        "Тетяна", "Денис", "Христина", "Богдан", "Софія"
    ]

    # Призначити від 1 до 3 випадкових курсів кожному
    for name in student_names:
        student = Student(name=name)
        assigned_courses = random.sample(courses, k=random.randint(1, 3))
        student.courses.add(assigned_courses)
    print("Успішно створено 5 курсів та 20 студентів!\n")


@db_session
def add_new_student(name: str, course_name: str):
    # Додаємо нового студента та запис його на курс
    course = select(c for c in Course if c.name == course_name).first()

    if not course:
        print(f"Курс '{course_name}' не знайдено!")
        return

    new_student = Student(name=name, courses=[course])
    print(f"Студента {new_student.name} додано на курс '{course_name}'.\n")


@db_session
def run_queries():
    # Запити до бази даних
    target_course_name = "Python Basics"
    students_in_course = select(
        s for s in Student if target_course_name in s.courses.name
    )[:]

    print(f"Студенти на курсі '{target_course_name}':")
    for s in students_in_course:
        print(f" - {s.name}")


    target_student_name = "Олексій"
    courses_for_student = select(
        c for c in Course if target_student_name in c.students.name
    )[:]

    print(f"Курси, на які записаний {target_student_name}:")
    for c in courses_for_student:
        print(f" - {c.name}")


@db_session
def update_and_delete():
    # Оновлення імені студента
    student_to_update = select(s for s in Student if s.name == "Марія").first()
    if student_to_update:
        old_name = student_to_update.name
        student_to_update.name = "Марія (Оновлено)"
        print(f"Ім'я змінено з '{old_name}' на '{student_to_update.name}'")

    # Оновлення назви курсу
    course_to_update = select(c for c in Course if c.name == "DevOps Intro").first()
    if course_to_update:
        course_to_update.name = "Advanced DevOps"
        print(f"Назву курсу оновлено на '{course_to_update.name}'")

    # Видалення студента з бази даних
    student_to_delete = select(s for s in Student if s.name == "Іван").first()
    if student_to_delete:
        print(f"Видаляємо студента: {student_to_delete.name}")
        student_to_delete.delete()


if __name__ == "__main__":
    init_seed_data()
    add_new_student("Тарас Шевченко", "Python Basics")
    run_queries()
    update_and_delete()