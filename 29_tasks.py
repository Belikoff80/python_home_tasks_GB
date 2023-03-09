# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2
# Нужно написать рекурсивную ф-цию только для левой части выражения!
# Результат нужно сверить с правой частью.
# Правой части выражения в рекурсивной ф-ции быть не должно!
# Решите через рекурсию. В задании нельзя применять циклы.

def sum_num(numb_str, n, num):
    if n == 1:
        numb_str += str(num - n+1)
    
        return (numb_str)
    else:
        numb_str += str(num - n+1) + '+'

        n -= 1 
        return sum_num(numb_str, n, num)

def sum_num1(numb_dig, n, num):
    if n == 1:

        numb_dig += (num - n+1)
        return numb_dig
    else:

        numb_dig += (num - n+1)
        n -= 1 
        return sum_num1(numb_dig, n, num)  

def sum_num2(numb_dig):
    return int(numb_dig*(numb_dig+1)/2)

numeric = int(input('Введите число: '))
print(f"{sum_num('', numeric, numeric)} = {numeric}*({numeric}+1)/2")
print(f'{numeric}*({numeric}+1)/2 = {sum_num2(numeric)}')
print(f"{sum_num('', numeric, numeric)} = {sum_num1(0, numeric, numeric)}")

if sum_num1(0, numeric, numeric) == sum_num2(numeric):
    print('Равенство доказано')
else:
    print('Правая илевая сторона не тождествены')
