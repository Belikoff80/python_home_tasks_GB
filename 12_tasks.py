# Задание 4. 
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Пример:
# Введите целые числа через пробел: 1 2 3 4
# Результат: 2 1 4 3

# Введите целые числа через пробел: 1 2 3
# Результат: 2 1 3

data_list = list(map(int,(i for i in input().split())))
i = 0
while i<=len(data_list) - 2:
    start_num = data_list[i]
    data_list[i] = data_list[i+1]
    data_list[i+1] = start_num
    i+=2
print(data_list)


