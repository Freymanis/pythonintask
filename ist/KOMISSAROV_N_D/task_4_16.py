# Задача 4. Вариант 16.
# Напишите программу, которая выводит имя, под которым скрывается Мартин Андерсен. 
#Дополнительно	необходимо	вывести	область	интересов	указанной личности,	место	рождения,	годы	рождения	и	смерти	(если	человек	умер), вычислить	возраст	на	данный	момент	(или	момент	смерти).
#Для	хранения	всех необходимых	данных	требуется	использовать	переменные.
#После	вывода информации	программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для выхода.


# Komissarov N.D.
# 15.04.17

from datetime import datetime

name = "Мартин Андерсен-Нексё"
name1 = "Martin Andersen Nexø"
intrest = "Прозаик, журналист"
birth = 1869
death = 1954
age = death-birth
place = "Дрезден, Германия"

print(name, "более известен, как датский писатель-коммунист и один из основателей Коммунистической партии Дании.", name1)
print("Место рождения:", place)
print("Год рождения:", birth)
print("Год смерти:", death)
print("Возраст:", age)
print("Область интересов:", intrest)
input("\n\nНажмите Enter, чтобы выйти.")
