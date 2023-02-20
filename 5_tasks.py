# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

digit = input('Введите 3-ех значное число: ')
b = 0
if len(digit) != 3 or digit.isdigit() != True:
    print ('Введено не верное число. Повторите ввод.')
else:
    for i in range(len(digit)):
        b+=int(digit[i])
    print(f'{digit} -> {b} ({digit[0]} + {digit[1]} + {digit[2]})')
