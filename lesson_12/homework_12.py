"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_int(a, b):
    return a + b


"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_list(list_integers: list):
    average_result = sum(list_integers) / len(list_integers)
    return average_result


"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string_arg: str):
    return string_arg[::-1]