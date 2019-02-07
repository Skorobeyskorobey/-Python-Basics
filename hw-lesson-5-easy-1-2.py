import os
print('Создание папок dir_1-dir_10')
print('***************************')

try:
    for m in range(1, 10):
        os.mkdir("dir_" + str(m))
except:
        print('такие папки уже есть')
list = os.listdir()
for m in list:
    print(m)
print('######################################################')
n = input('Для удаления папок dir_1-dir_10, нажмите клавишу Enter')
print(n)
try:
    for m in range(1, 10):
        os.rmdir("dir_" + str(m))
except:
    print("файлы уже удалены")
list = os.listdir()
for m in list:
    print(m)
print('**************************')
print('Папки dir_1-dir_10 удалены')
