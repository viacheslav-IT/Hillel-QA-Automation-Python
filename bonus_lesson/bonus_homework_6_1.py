# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

new_string = input("Please enter a new string: ")
counter = 0
for i in new_string:
    if new_string.count(i) == 1:
        counter += 1
print(f'Кількість унікальних символів в строці: {counter}')
if counter > 10:
    print(True)
else:
    print(False)


