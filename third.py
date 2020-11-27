# Найти среднее арифметическое трех последних элементов списка.
import random

list_length = int(input("Размер списка: "))
my_list = []
for i in range(list_length):
    numb = random.randint(0, 99)
    my_list.append(numb)
print(my_list)
my_list.reverse()
print((my_list[0] + my_list[1] + my_list[2])/3)

