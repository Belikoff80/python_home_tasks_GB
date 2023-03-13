# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# min_val = int(input('мин зн диап= '))
# max_val = int(input('макс зн диап= '))

def list_gen(start, finish):
    if finish > 0 and start >= 0:
        A=[(start + 1 + (i)) for i in range(finish - start)]
    elif finish >= 0 and start < 0:
        A=[(start + 1 + (i)) for i in range(finish - start - 1)]
    elif finish < 0 and start < 0:
        A=[(start + 1 + (i)) for i in range(start*(-1) - finish*(-1) - 1)]
    return A
def range_index(min_range, max_range):
    range_list = list_gen(int(input('стартовое значение списка= ')),int(input('макс значение списка= ')))
    data_list = list_gen(min_range, max_range+1)
    i_range = []
    for i in range (len(range_list)):
        if range_list[i] in data_list:
            i_range.append(i)
        else:
            i += 1
    return i_range

  
print(range_index(int(input('введите стартовое значение диапазона: ')), 
                  int(input('введите значение окончания диапазона: '))))




    