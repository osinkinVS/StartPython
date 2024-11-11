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

# # Задача 3. Двумерный список
# print('Задача 3.')
# my_list = [[j_num for j_num in range(i_list, 13, 4)] for i_list in
# range(1, 5)]
# print(my_list)
# # Альтернативный вариант решения с использованием фиксированных смещений
# second_answer = [[value, value + 4, value + 8] for value in range(1,
# 5)]
# print(second_answer)

# # Задача 4. Список списков
# print('Задача 4.')
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# output = [digit
#     for each_list in nice_list
#     for each_list_2 in each_list
#     for digit in each_list_2]
# print(output)

# # Задача 5. Шифр Цезаря
# print('Задача 5.')
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Функция для шифрования текста по методу Цезаря
def caesar_cipher(string, user_shift):
# Создание списка зашифрованных символов
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)]
         if sym in alphabet else sym)
        for sym in string]
# Преобразование списка символов в строку
    new_str = ''.join(char_list)
    return new_str
# Ввод пользователем исходного сообщения и сдвига
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
# Шифрование сообщения
output_str = caesar_cipher(input_str, shift)
# Вывод зашифрованного сообщения
print('Зашифрованное сообщение:', output_str)