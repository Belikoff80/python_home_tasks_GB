# *Задача 20: * В настольной игре Скрабл (Scrabble) 
# каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 
# 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 
# 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, 
# либо только русские буквы.

rus = {}
list1 =  ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'] 
list2 = ['Д', 'К', 'Л', 'М', 'П', 'У'] 
list3 = ['Б', 'Г', 'Ё', 'Ь', 'Я'] 
list4 = ['Й', 'Ы'] 
list5 = ['Ж', 'З', 'Х', 'Ц', 'Ч'] 
list6 = ['Ш', 'Э', 'Ю']
list7 = ['Ф', 'Щ', 'Ъ'] 
list8 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'] 
list9 = ['D', 'G'] 
list10 = ['B', 'C', 'M', 'P'] 
list11 = ['F', 'H', 'V', 'W', 'Y'] 
list12 = ['K'] 
list13 = ['J', 'X'] 
list14 = ['Q', 'Z'] 
# функция для перевода списка букв и их стоимость в очках в словарь
def list_to_dict(list_n, rate):
    dict_n = {}
    for i in range(len(list_n)):
        dict_n[list_n[i]] = rate
    return dict_n
# функция для объединения словарей 
def merged_dict (a,b,c,d,e,f,g, h, i, j, k, l, m, n):
     merg_dict = {**a,**b,**c,**d,**e,**f,**g, **h,**i,**j,**k,**l,**m,**n}
     return merg_dict

rus = merged_dict(list_to_dict(list1,1), list_to_dict(list2, 2), list_to_dict(list3, 3), list_to_dict(list4, 4), 
list_to_dict(list5, 5), list_to_dict(list6, 8), list_to_dict(list7, 10), 
list_to_dict(list8, 1), list_to_dict(list9, 2), list_to_dict(list10, 3), list_to_dict(list11, 4), list_to_dict(list12, 5), 
list_to_dict(list13, 8), list_to_dict(list14, 10))

count = 0
for i in input('Введите слово: ').upper():
        if i in rus:
            count += rus[i]
print(count)

