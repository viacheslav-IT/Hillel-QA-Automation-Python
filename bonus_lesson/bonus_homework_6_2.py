# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    new_string = input("Enter a word containing the letter 'h': ")
    if 'h' in new_string.lower():
        print('Your word contains "h" letter')
        break