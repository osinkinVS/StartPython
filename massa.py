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