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