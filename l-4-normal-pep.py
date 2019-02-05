####
import re  # задание 1
name = input('Введите ваше имя : ')
surename = input('Введите вашу фамилию : ')
email = input('Введите ваш email: ')
if re.match('^[А-Я]{1,1}', name) is not None:
    if re.match('^[А-Я]{1,1}', surename) is not None:
        if re.findall('[a-z0-9_]+@+[a-z0-9]+\.(ru|com|org)', name) is not None:
            print('Приветствуем вас, {} {}! Ваш email: {}'
                  .format(name, surename, email))
else:
    print('Ваши данные  не верны!')
