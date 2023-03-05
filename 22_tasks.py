# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random
num_elem1 = int(input('Введите количество элементов в 1ом множество: '))
num_elem2 = int(input('Введите количество  элементов во 2ом множестве: '))
def list_generatic(n):
    list_inter = []
    for _ in range(n):
        num_gen = random.randint(0,30)
        list_inter.append(num_gen)
    return list_inter

num1 = (list_generatic(num_elem1))
num2 = (list_generatic(num_elem2))
num = num1 + num2
numb = set(num)
numb_fixed = frozenset(numb)
print(*numb_fixed)



