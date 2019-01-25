name = input("Ведите Ваше имя и фамилию   ")
print ("Привет ", name)
age = int(input("Ведите Ваш возраст   "))
weight = int(input("Ведите Ваш вес   "))
print (name, "  возраст: ", age, " вес: ", weight)
if(50 < weight < 120) and age < 30:
    print(" Да Вы в хорошем состоянии !")
elif(50 < weight < 120) and (30 < age < 50):
    print(" Да Вы  красавчик!")
elif (weight < 50 or weight > 120) and age > 40:
    print(" Да Вы должны пройти врачебный осмотр !")
elif (weight < 50 or weight > 120) and age > 30:
    print(" Да Вы должны начать вести правильный образ жизни !")
if (250 > weight > 120):
    print(" Да ещё Вы Жиробас !")
if (20 < weight < 40):
    print(" Да ещё Вы Дистрофан !")
