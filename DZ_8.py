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