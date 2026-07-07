# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def get_generator(n):
    return (x for x in range(n + 1) if x % 2 == 0)


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# Реалізуйте ітератор для зворотного виведення елементів списку.
class IteratorReverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        item = self.data[self.index]
        self.index -= 1
        return item


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        current_number = self.current
        self.current += 2

        return current_number


# Напишіть декоратор, який логує аргументи та результати викликаної функції.
from functools import wraps


def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функція '{func.__name__}'")
        print(f"Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Функція '{func.__name__}' повернула: {result}")
        return result

    return wrapper
