# # Задача 1. Найти множества
# print('Задача 1. Найти общее')
# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# all_elem = array_1 + array_2 + array_3
# new = []
# for elem in all_elem:
#     if elem not in new and all(elem in array for array in 
#                                [array_1, array_2, array_3]):
#         new.append(elem)
# print('Решение без множеств: ', *new)

# new_set = set(array_1) & set(array_2) & set(array_3)
# print('Решение со множеством: ', *new_set)

# print('Задача 1.1 Найти униальные элементы из списка')
# new_2 = []
# for elem in array_1:
#     if elem not in array_2 and elem not in array_3:
#         new_2.append(elem)
# print('Решение без множеств: ', *new_2)

# set_new = set(array_1) - set(array_2) - set(array_3)
# print('Решение со множеством: ', *set_new)

# # Задача 2. Палиндром
# print('Задача 2.')
# def is_poly(string):
#     char_dict = dict()
#     for i_sym in string:
#         char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
#     odd_count = 0 
#     for i_value in char_dict.values():
#         if i_value % 2 != 0:
#             odd_count +=1
#     return odd_count <= 1 
# my_string = input('Введите строку: ').lower()
# if is_poly(my_string):
#     print('Можно сделать палиндром')
# else:
#     print('Нельзя сделать палиндром')

# Задача 3. Словарь синонимов
print('Задача 3.')
synonyms_dict = dict()
par = int(input('Введите количество пар слов: '))
for i in range(par):
    first, second = input(f'{i +1} пара:').lower().split(' - ')
    synonyms_dict[first] = second
    synonyms_dict[second] = first
while True:
    word = input('введите слово: ').lower()
    if word in synonyms_dict:
        print('Синоним: ', synonyms_dict[word].capitalize())
        break
    else:
        print('Такого слова в словаре нет.')