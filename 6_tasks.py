# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


summa = int(input('Введите сколько всего жураликов сделано: '))
x = int (summa / 6)
if summa%6!=0 or summa < 6:
    print('Неверное значение суммы. Введите число кратное 6 и более или равное 6: ')
else:
    print(f'{summa} -> {x}  {4*x}  {x}')