# # Задача 1. Сумма чисел
# print('Задача 1.')
# import os
# # Открываем входной файл для чтения
# numbers_file = open("numbers.txt", "r", encoding="utf-8")
# # Инициализируем переменную для хранения суммы чисел
# total_sum = 0
# # Читаем файл построчно
# for line in numbers_file:
# # Разбиваем строку на части, используя пробелы и новые строки в качестве разделителей
# # Преобразуем каждую часть в целое число и накапливаем сумму
#     numbers = [int(num) for num in line.split() if num]
#     total_sum += sum(numbers)
# # Закрываем файл после чтения
# numbers_file.close()
# # Открываем выходной файл для записи
# sum_file = open("answer.txt", "w", encoding="utf-8")
# # Записываем сумму в выходной файл
# sum_file.write(str(total_sum))
# # Закрываем выходной файл
# sum_file.close()

# # Задача 2. Сумма чисел
# print('Задача 2.')
# text_py = open('zen.txt', 'r')
# lines = text_py.readlines()
# text_py.close()
# for line in reversed(lines):
#     print(line.strip())

# # Задача 3. Турнир
# print('Задача 3.')
# with open('first_tour.txt', 'r') as first_tour:
#     lines = first_tour.readlines()
#     k = int(lines[0])
#     remembers = {} # хранение участников
#     second_tour = {} # хранение прошедших во второй тур
#     count = 1 

# for line in lines[1:]:
#     data = line.strip().split()
#     name = f'{data[1] [0]}. {data[0]}'
#     score = int(data[-1])
#     remembers[name] = score

# for player, score in remembers.items():
#     if score > k:
#         second_tour[player] = score

# sorted_filter_player = dict(sorted(second_tour.items(), key=lambda x: x[1], reverse=True))

# with open('second_tour_.txt', 'w') as file:
#     file.write(f'{len(sorted_filter_player)}\n')
#     for player, score in sorted_filter_player.items():
#         file.write(f'{count}) {player} {score}\n')
#         count +=1

# # Задача 4. Частотный анализ
# print('Задача 4.')
# english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# total_letters = 0
# # Открываем файл text.txt и считываем текст
# with open("text.txt", "r") as file:
#     text = file.read().lower() # Приводим текст к нижнему регистру
# # Создаем словарь для подсчета количества каждой буквы
# letter_count = {letter: 0 for letter in english_alphabet}
# # Подсчитываем количество вхождений каждой буквы
# for char in text:
#     if char in english_alphabet:
#         letter_count[char] += 1
#         total_letters += 1
# # Вычисляем частоту встречаемости каждой буквы
# letter_freq = {letter: (count / total_letters) for letter, count in
# letter_count.items() if count > 0}
# # Сортируем буквы по убыванию частоты и по алфавиту при равенстве частоты
# sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))
# # Записываем результат в файл analysis.txt
# with open("analysis.txt", "w") as file:
#     for letter, freq in sorted_letters:
#         file.write(f"{letter} {freq:.3f}\n")

import zipfile
# Открываем архив и ищем текстовый файл
with zipfile.ZipFile("voina-i-mir.zip", "r") as zip_ref:
# Получаем список файлов в архиве и выбираем первый текстовый файл
    file_name = [name for name in zip_ref.namelist() if name.endswith('.txt')][0]
# Открываем выбранный файл и читаем его содержимое
    with zip_ref.open(file_name) as file:
        text = file.read().decode('utf-8')
# Инициализируем словарь для подсчета количества символов
char_count = {}
# Подсчитываем количество вхождений каждого символа
for char in text:
    if char.isalpha(): # Учитываем только буквы
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
# Сортируем символы по частоте (в убывании) и по алфавиту при равенстве частоты
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
# Записываем результаты в файл
with open("statistik.txt", "w", encoding="utf-8") as file:
    for char, freq in sorted_chars:
        file.write(f"{char}: {freq}\n")