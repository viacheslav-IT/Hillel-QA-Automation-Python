# Завдання 1:
# Візьміть два файли csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result.csv

import csv
unique_rows = set()

# Считуємо файл random.csv
with open('random.csv', 'r', encoding='utf-8', newline='') as csvfile_1:
    reader_1 = csv.reader(csvfile_1)
    for row in reader_1:
        unique_rows.add(tuple(row))

# Считуємо файл random-michaels.csv
with open('random-michaels.csv', 'r', encoding='utf-8', newline='') as csvfile_2:
    reader_2 = csv.reader(csvfile_2)
    for row in reader_2:
        unique_rows.add(tuple(row))

# Записуємо дані (без дублікатів) у новий файл
with open('result.csv', 'w', encoding='utf-8', newline='') as csvfile_3:
    writer = csv.writer(csvfile_3)
    for row in unique_rows:
        writer.writerow(row)