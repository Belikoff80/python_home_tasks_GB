# Задание 2.

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и только арифметические операции.
# Не используйте взятие по индексу.

# Пример:
# Ведите целое положительное число: 123456789
# Самая большая цифра в числе: 9
digit = input('Введите целое положительное число: ')
max_num = 0
i = 0
while i!=len(digit):
    
    if max_num<int(digit[i]):
        max_num = int(digit[i])
        i+=1
    else:
        i+=1
print(f'Самая большая цифра в числе: {max_num}')