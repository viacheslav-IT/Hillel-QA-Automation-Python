# З файлу hblog.txt відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400

def filter_key_str(file):
    with open(file, 'r', encoding='utf-8') as f_1:
        with open('hb_test.log', 'w', encoding='utf-8') as f_2:
            for line in f_1:
                if 'Key TSTFEED0300|7E3E|0400' in line:
                    f_2.write(line)

filter_key_str('hblog.txt')


# Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
# - для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
# - для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log

from datetime import datetime


def analize_heartbeat(input_file, output_file):
    prev_time = None

    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'a', encoding='utf-8') as f_out:
            for line in f_in:
                timestamp_value = line.find("Timestamp ")
                if timestamp_value != -1:
                    time_str = line[timestamp_value + 10: timestamp_value + 18]

                    curr_time = datetime.strptime(time_str, "%H:%M:%S")

                    if prev_time is not None:
                        delta = (prev_time - curr_time).total_seconds()

                        if 31 < delta < 33:
                            f_out.write(f"WARNING: heartbeat diff {delta} sec at {time_str}\n")
                        elif delta >= 33:
                            f_out.write(f"ERROR: heartbeat diff {delta} sec at {time_str}\n")

                    prev_time = curr_time


analize_heartbeat('hb_test.log', 'analize_heartbeat.log')
