# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# a.	Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), 
# количество (quantity), цена (price),
# покупатель (buyer), дата (date). 
# Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
# При записи данных указать величину отступа в 4 пробельных символа;
# b.	Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
import json

def write_order_to_json():
    a = input('type the item: ')
    b = input('type the nums: ')
    c = input('type the price: ')
    d = input('type the buyer: ')
    e = input('type the date: ')  

    dict_to_json = {
    "товар": a,
    "количество": b,
    "цена": c,
    "покупатель": d,
    "дата": e}
    with open('orders.json', 'w') as f_n:
        # f_n.write(json.dumps(dict_to_json))
        json.dump(dict_to_json, f_n, indent=4)
    with open('orders.json') as f_n:
        print(f_n.read())

write_order_to_json()
