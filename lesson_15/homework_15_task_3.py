# Завдання 3:
# Для файла groups.xml створіть функцію пошуку по group
# і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_timing_exbytes_incoming(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        count = 0

        for group in root.findall('.//group'):
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                incoming_value = incoming.text
                logging.info(f"Знайдено значення timingExbytes/incoming: {incoming_value}")
                count += 1

    except FileNotFoundError:
        logging.error(f"Файл {xml_file} не знайдено!")

get_timing_exbytes_incoming('groups.xml')