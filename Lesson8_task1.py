# 1.	
# Задание на закрепление знаний по модулю CSV. 
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt,
# info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. 
# Для этого:
# a) Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, 
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных 
# выражений извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». 
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list,
# os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», 
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

# b.	Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
# В этой функции реализовать получение данных через вызов функции get_data(), 
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# 
# c.	Проверить работу программы через вызов функции write_to_csv().


#1. Функция создае файл txt со столбцами:  Название ОС, Код продукта, Изготовитель системы, Тип системы.
# В столбцах вписаны значения из файлов аргументов функции.
# +Функция выводит данные в виде списка списков
import csv

def get_data(*args):

    os_prod_list = []
    os_name_list = [] 
    os_code_list = [] 
    os_type_list = []
    main = []
   

    data = [*args]
    
    for i in range (len(data)):
        with open(data[i]) as f_n:
            for row in f_n:
                if 'Название ОС' in row:
                    os_name_list.append(((row.split(':')[1]).split('\n')[0]).strip())
                    main.append(row.split(':')[0])
                elif 'Код продукта' in row:
                    os_code_list.append(((row.split(':')[1]).split('\n')[0]).strip())
                    main.append(row.split(':')[0])
                elif 'Изготовитель системы' in row:
                    os_prod_list.append(((row.split(':')[1]).split('\n')[0]).strip())
                    main.append(row.split(':')[0])
                elif  'Тип системы' in row:
                    os_type_list.append(((row.split(':')[1]).split('\n')[0]).strip())
                    main.append(row.split(':')[0])
    #  
    
    g_of_str = [os_name_list, os_code_list, os_prod_list, os_type_list]
    f_end = open('main_data.txt', 'w')
    k = (str(main))+'\n'
    f_end.write(k)
    f_end.close()
    num_str1 = []
    num_str1.append(main[0:4])
    for i in range(len(data)):
        k=0
        num_str = []
        
        for j in range(len(g_of_str)):
            num_str.append(g_of_str[j][i])
        num_str1.append(num_str)
        f_end = open('main_data.txt', 'a')
        k = (str(num_str))+'\n'
        f_end.write(k)
        f_end.close()  
    
    return(num_str1)        

print(get_data('info_1.txt', 'info_2.txt', 'info_3.txt' ))

# 2.
def write_to_csv(*args):

    data = get_data(*args )
    with open('kp_data_write.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)

    with open('kp_data_write.csv') as f_n:
        return(f_n.read())

print(write_to_csv('info_1.txt', 'info_2.txt', 'info_3.txt'))
    
