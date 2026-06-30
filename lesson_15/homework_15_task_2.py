# Завдання 2:
# Провалідуйте, чи усі файли є валідними json.
# Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json.log

import json
import logging
logging.basicConfig(
            filename = 'json.log',
            level = logging.ERROR,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

json_list = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']

for json_file in json_list:
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError as e:
        logging.error(f"Файл {json_file} невалідний. Помилка: {e}")