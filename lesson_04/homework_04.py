adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3


# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_task_01 = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_task_02 = adwentures_of_tom_sawer_task_01.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_task_03 = ' '.join(adwentures_of_tom_sawer_task_02.split())


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for i in adwentures_of_tom_sawer_task_03:
    if i == "h":
        count += 1
print(f'Літера "h" зустрічається в тексті {count} разів')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer_task_05 = adwentures_of_tom_sawer_task_03.split()
count = 0
for i in adwentures_of_tom_sawer_task_05:
    if i.istitle():
        count += 1
print(f'{count} слів у тексті починається з великої літери.')


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer_task_06_list = adwentures_of_tom_sawer_task_03.split()
count = 0
for i in adwentures_of_tom_sawer_task_06_list:
    if i == 'Tom':
        count += 1
        if count == 2:
            first_index = adwentures_of_tom_sawer_task_06_list.index('Tom')
            second_index = adwentures_of_tom_sawer_task_06_list.index('Tom', first_index + 1, len(adwentures_of_tom_sawer_task_06_list) - 1)
            print(f"Слово 'Tom' зустрічається вдруге на позиції {second_index}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_task_03.split('.')
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print((adwentures_of_tom_sawer_sentences[3]).lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
count = 0
for i in adwentures_of_tom_sawer_sentences:
    if (i.strip()).startswith("By the time"):
        count += 1
print(f'Кількість речень, які починаються з "By the time": {count}')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences_task_10 = adwentures_of_tom_sawer_sentences[-2].split()
print(f'Кількість слів в останньому реченні: {len(adwentures_of_tom_sawer_sentences_task_10)}')