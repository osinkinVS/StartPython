# # Задача 1. Старые и ноые видеокарты
# print('Задача 1.')
# video = int(input()) # Количество видеокарт 
# vcards = []
# vcards_new = [] 
# max_num = 0
# for item in range (video):
#     vcards.append(int(input(f'Видеокарта {item + 1}: ')))
#     if vcards[item] > max_num:
#         max_num = vcards[item]
# for item in range (video): 
#     if vcards[item] != max_num:
#         vcards_new.append(vcards[item])
# print('Старый список видеокарт: [', end=' ')
# for item in range(video):
#     print(vcards[item], end=' ')
# print(']')
# print('Новый список видеокарт: [', end=' ')
# for item in range(len(vcards_new)):
#     print(vcards_new[item], end=' ')
# print(']')

# # Задача 2. Кино
# print('Задача 2.')
# films = ['Крепкий орешек', 'Назад в будущее', 
#         'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 
#         'Мементо', 'Отступники', 'Деревня']
# my_list = []
# movie_check = int(input('Сколько фильмов вы хотите добавить? '))
# for _ in range (movie_check):
#     movie = (input('Введите название фильма: '))
#     if movie in films:
#         my_list.append(movie)
#     else:
#         print(f'Error: фильма {movie} у нас нет')
# print(f'Ваш список любимых фильмов: {my_list}')

# # Задача 3. Сортировка
# print('Задача 3.')
# N = int(input('Введите количество N чисел:'))
# list = []
# for n in range (N):
#     list.append(int(input(f'Введите число {n + 1}: ')))
# print('Изначальный список:', list)
# for i in range (len(list)-1):
#     for j in range (len(list)-1-i):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
# print('Отсортированный список:', list)

# # Задача 4. Товары
# print('Задача 4.')
# goods={'Лампа': '12345','Стол': '23456','Диван': '34567','Стул': '45678',}
# store = { '12345': [{'quantity': 27, 'price': 42},],
#  '23456': [
#  {'quantity': 22, 'price': 510},
#  {'quantity': 32, 'price': 520},],
#  '34567': [
#  {'quantity': 2, 'price': 1200},
#  {'quantity': 1, 'price': 1150},],
#  '45678': [
#  {'quantity': 50, 'price': 100},
#  {'quantity': 12, 'price': 95},
#  {'quantity': 43, 'price': 97},],}
# for item_name in goods.keys():
#     item_code = goods[item_name]
#     total_quantity = 0
#     total_cost = 0
#     for entry in store[item_code]:
#         total_quantity += entry['quantity']
#         total_cost += entry['price'] * entry['quantity']
#     print('{} - {} штук, стомимость {} рубля(ей).'.format(item_name, 
#     total_quantity, total_cost))