# 3.	Определить, какие из слов «attribute», «класс», «функция», 
# «type» невозможно записать в байтовом типе.

check1= ['attribute', 'класс', 'функция', 'type']
for i in range(len(check1)):
    check2 = check1[i].encode('ascii', 'replace')
    if b'?' in check2:
        print(f'<{check1[i]}> невозможно записать в байтовом типе')
    else:
        print(f'<{check1[i]}> в байтовом типе: {check2}', type(check2))