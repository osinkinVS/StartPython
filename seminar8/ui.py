from logger import input_data, print_data

def interface():
    print('Добрый день! Это специальный бот-справочник \n 1 - Запись данных \n 2 - Вывод данных ')
    command = int(input('Выберите действие '))

    while command != 1 and command != 2:
        print('Неправильный ввод')
        command = int(input('Выберите вариант 1 или 2 ')) 
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()