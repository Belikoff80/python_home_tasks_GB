# 4.	Преобразовать слова «разработка», «администрирование», «protocol», 
# «standard» из строкового представления в байтовое 
# и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']
words_back = []
for i in words:
    words_b = i.encode('utf-8')
    words_back.append(words_b)
    print(f'<<{i}>> в байтовом типе: {words_b}', type(words_b))
print()
for i in words_back:
    k = i.decode('utf-8')

    print(f'<<{i}>> в utf-8 типе: {k}', type(k))
    print()


