# Задание на закрепление знаний по модулю yaml. 
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. 
# Для этого:
# a.	Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
# второму — целое число, 
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке 
# ASCII (например, €);
# b.	Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, 
# а также установить возможность работы с юникодом: allow_unicode = True;
# c.	Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
import pyyaml as yaml

dictfile = {'food':['apple', 'orange', 'water'], 'num' : 3, 'emp1': {'name': 'Timur', 'job': 'Teacher'}}

with open('file.yaml', 'w') as f_n:
    yaml.dump(dictfile, f_n, default_flow_style=False)

with open('file.yaml') as f_n:
    print(f_n.read())
