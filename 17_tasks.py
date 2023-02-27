# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

# List method

month_name = ['Январь','Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 
              'Октябрь', 'Ноябрь', 'Декабрь']
season_month = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 
                9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
flag = False
while flag != True:
    month_digit = int(input('Введите номер месяца: '))
    if month_digit < 1 or month_digit > 12:
        print('Введите число в диапазоне от 1 до 12')
    else:
        print (f'Название месяца: {month_name[month_digit-1]}')
        print (f'Сезон: {season_month[month_digit]}')
        flag = True

