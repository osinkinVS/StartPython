# Задача 1. Старые и ноые видеокарты
video = int(input()) # Количество видеокарт 
vcards = []
vcards_new = [] 
max_num = 0
for item in range (video):
    vcards.append(int(input(f'Видеокарта {item + 1}: ')))
    if vcards[item] > max_num:
        max_num = vcards[item]
for item in range (video): 
    if vcards[item] != max_num:
        vcards_new.append(vcards[item])
print('Старый список видеокарт: [', end=' ')
for item in range(video):
    print(vcards[item], end=' ')
print(']')
print('Новый список видеокарт: [', end=' ')
for item in range(len(vcards_new)):
    print(vcards_new[item], end=' ')
print(']')
