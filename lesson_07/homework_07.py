# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_int(a, b):
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_list(list_integers: list):
    average_result = sum(list_integers) / len(list_integers)
    return average_result


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string_arg: str):
    return string_arg[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_word(words_list: list):
    sorted_list = sorted(words_list, key = lambda x: len(x))
    return (sorted_list[-1])


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        index_str2 = str1.find(str2)
        return index_str2
    elif str2 not in str1:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
def word_counter(string_arg: str):
    count = 0
    for i in string_arg:
        if i == "h":
            count += 1
    return f'Літера "h" зустрічається в тексті {count} разів'


# task 8
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
def word_title_counter(string_arg: str):
    list_string_elements = string_arg.split()
    count = 0
    for i in list_string_elements:
        if i.istitle():
            count += 1
    return f'{count} слів у тексті починається з великої літери.'


# task 9
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
def tom_word_index(string_arg: str):
    list_string_elements = string_arg.split()
    count = 0
    for i in list_string_elements :
        if i == 'Tom':
            count += 1
            if count == 2:
                first_index = list_string_elements.index('Tom')
                second_index = list_string_elements.index('Tom', first_index + 1, len(list_string_elements) - 1)
                return f"Слово 'Tom' зустрічається вдруге на позиції {second_index}"


# task 10
""" Перевірте чи починається якесь речення з "By the time".
"""
def phrase_present(string_arg: str):
    count = 0
    list_string = string_arg.split('.')
    for i in list_string:
        if i.strip().startswith("By the time"):
            count += 1
    return f'Кількість речень, які починаються з "By the time": {count}'

