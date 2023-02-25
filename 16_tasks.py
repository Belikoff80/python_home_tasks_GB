# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
num_range = int(input('Введите значение максимального числа: '))
k = 1
digit = 0
whole_pow = []

while digit < num_range-2:
    digit = 2*k
    whole_pow.append(digit)
    k+=1
print(f'Вывод целых степеней двойки: {whole_pow}')