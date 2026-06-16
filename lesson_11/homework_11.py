new_list = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

def sum_elements(lst: list):
    count = 0
    for element in lst:
        count += 1
        try:
            total = sum(map(int, element.split(',')))
            print(f'Сума всіх чисел {count} елементу в списку: {total}')
        except Exception as e:
            print(f'Не можу це зробити!: {e}')

sum_elements(new_list)