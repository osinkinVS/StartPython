# # Задача 1. Посчитать количество положительых оценок
# print('Задача 1.')
# p = 0
# n = 0
# a = int(input('Введите оценку:'))
# while a!= 0:
#     if a > 0:
#         p+=1
#     else: 
#         n+=1
#     a = int(input('Введите оценку:'))
# print ('Количество положительных оценок:', p)
# print ('Количество отрицательных оценок:', n)

# # Задача 2. Рабочий день
# print('Задача 2. Начался восьмичасовой день')
# hour = 1
# task = 0
# shop = 0
# while hour <=8:
#     a = int(input('Сколько задач решите за этот час?'))
#     task +=a 
#     b = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет):'))
#     if b == 1:
#         shop = 1
#     hour +=1
# print('Количество решёных задач:', task)
# if shop == 1:
#     print('Нужно зайти в магазин')
# else:
#     print('В магазин можно не заходить')

# # Задача 3. Угадай число
# print('Задача 3.')
# number = 5 
# count = 0
# while True:
#     num_count = int(input('Введите число:'))
#     if num_count > number:
#         print('Это число больше, чем нужно. Попробуй ещё раз)')
#     elif num_count < number:
#         print('Это число меньше, чем нужно. Попробуй ещё раз)')
#     else:
#         print('Вы угадали. Ура!')
#         break

# Задача 4. Посчитать средную зарплату 
print('Задача 4.')
salary_year = 0
for month in range(1,13):
    salary_month = int(input('Введите зарплату за месяц:'))
    salary_year += salary_month
average_year = salary_year/12
print('Средняя зарплата за год составляет:', average_year)
