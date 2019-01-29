#
print('Задача 1')
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
for x in range(0, len(fruits)):
    print((x+1), '{:>10}'.format(fruits[x]))
#
print('Задача 2')
list_1 = {'1', '2', '3', '11', '12', '14', '123', '13'}
list_2 = {'1', '2', '3', '14', '15', '13'}
list_3 = list_1 - list_2
print('Первый список', list(list_1))
print('Второй список', list(list_2))
print('Оставшиеся после удаления элементы первого списка', list(list_3))
#
print('Задача 3')
list_1 = [4, 9, 15, 63, 3, 26]
print ('Произвольный список целых чисел  ', list_1)
list_2 = []
name_end = len(list_1)
for a in range(name_end):
    if list_1[a] % 2 == 0:
        list_2.append(list_1[a] / 4)
    else:
        list_2.append(list_1[a] * 2)
        print(list_2)
