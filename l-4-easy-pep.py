######
list_1 = [5, 7, 4, 10]            # 1 задание #
list_2 = [a ** 2 for a in list_1]
print(list_2)
######
list_1 = ['виноград', 'папайя', 'арбуз', 'апельсин']  # 2 задание
list_2 = ['апельсин', 'папайя', 'яблоко', 'груша']
list_2 = list(set(list_1) & set(list_2))
print(list_2)
######
list_1 = [3, 7, 9, -11, 10, -7, 6, -32, 0]  # 3 задание
list_2 = [el for el in list_1 if el % 3 == 0 and el >= 0 and el % 4 != 0]
print(list_2)
