# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def count_list_numbers(lst: list[int]):
    sum_numb = 0
    for i in lst:
        if i % 2 == 0:
            sum_numb += i
    print(f'Сумма усіх ПАРНИХ чисел в лісті: {sum_numb}')