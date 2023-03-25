# 5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com 
# и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
args = ['ping', 'yandex.ru']
check = subprocess.Popen(args, stdout=subprocess.PIPE)
print('Пинг веб-ресурса yandex.ru:')
for line in check.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
print('Пинг веб-ресурса youtube.com:')
args1 = ['ping', 'youtube.com']
check1 = subprocess.Popen(args1, stdout=subprocess.PIPE)

for line in check1.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))