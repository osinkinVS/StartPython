# # Задача 1. Гласные буквы 
# print('Задача 1.')
# text = input('Введите текст: ').lower()
# glas = 'уеыаоэяиюё'
# vowels = [i for i in text if i in glas]
# print('Список гласных букв: ', vowels)
# print('Длина списка:', len(vowels))

# # Задача 2. Случаные соревнования 
# print('Задача 2.')
# import random
# first = [round(random.uniform(5, 10), 2) for _ in range(20)]
# second = [round(random.uniform(5, 10), 2) for _ in range(20)]
# win = [
#     first[i] if first[i] > second [i]
#     else second[i]
#     for i in range(20)]
# print('Первая команда:', first)
# print('Вторая команда:', second)
# print('Победители тура:', win)
