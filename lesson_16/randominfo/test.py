from randominfo import Person

try:
    person = Person()
    print(person.full_name, person.gender, person.country, person.address)
except IndexError as e:
    print(f'Отримуємо наступну помилку: {e}')
