# # Задача 1. Новые списки
# print('Задача 1.')  
# from functools import reduce

# floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers = [22, 33, 10, 6894, 11, 2, 1]

# map_result = list(map(lambda x: round(x**3, 3), floats))
# filter_result = list(filter(lambda name: len(name) >= 5, names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

# print(map_result)
# print(filter_result)
# print(reduce_result)

# # Задача 2. ZIP
# print('Задача 2.') 
# from typing import List, Tuple
# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), strings, numbers))
# print(results) 

# # Задача 3. Палиндром
# print('Задача 3.') 
# from collections import Counter
# def can_be_poly(val: str) -> bool:
#     count = Counter(val)
#     odd_count = len(list(filter(lambda x: x % 2, count.values())))
#     return odd_count < 2
# print(can_be_poly('eerru'))
# print(can_be_poly('abbcba')) 
# print(can_be_poly('abbbc')) 

# # Задача 4. Уникальный шифр
# print('Задача 4.') 
# def unique(string):
#     lower_str = string.lower()
#     unique_char = list(filter(lambda c: lower_str.count(c.lower()) == 1, lower_str))
#     print(unique_char)
#     return len(unique_char)
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = unique(message)
# print("Количество уникальных символов в строке:", unique_count)