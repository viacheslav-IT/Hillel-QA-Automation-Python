# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

new_string = input("Please enter a new string: ")
unique_words = len (set(new_string.lower()))
print(f'Кількість унікальних символів в строці: {unique_words}')
if unique_words > 10:
    print(True)
else:
    print(False)


