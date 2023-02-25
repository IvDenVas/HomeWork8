# Создать телефонный справочник с 
# возможностью импорта и экспорта данных в 
# формате .txt. Фамилия, имя, отчество, номер 
# телефона - данные, которые должны находиться 
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в 
# текстовом файле
# 3. Пользователь может ввести одну из 
# характеристик для поиска определенной 
# записи(Например имя или фамилию 
# человека)
# 4. Использование функций. Ваша программа 
# не должна быть линейной

def create_person():
    data = open('file.txt', 'a', encoding='utf-8')
    name = str(input("Введите имя: " ))
    patronymic = str(input("Введите отчество: "))
    last_name = str(input("Введите фамилию: "))
    number = str(input("Введите номер телефона: "))
    data.write(last_name + ' ' + name + ' ' + patronymic + ' ' + number + '\n')
    data.close()

def show_all():
    path = 'file.txt'
    data = open('file.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

def search():
    path = 'file.txt'
    data = open('file.txt', 'r', encoding='utf-8')
    res = str(input("Введите поисковые данные: "))
    for line in data:
        if res in line:
            print(line)
    data.close()
    return print

def delete():
    with open('file.txt', "r",encoding='utf-8') as file:
        temp = file.readlines()
        inp = str(input("Введите поисковые данные: "))
        res = []
        for line in temp:
            if inp not in line:
                res.append(line)
            else:
                print(f'Удалено: {line}')

    with open('file.txt', "w") as file:
        file.writelines(res)

def change():
    with open('file.txt', "r", encoding='utf-8') as file:
        temp = file.readlines()
        inp = str(input("Введите изменяемое значение: "))
        res = []
        for line in temp:
            if inp in line:
                if input(f'Здесь заменить? {line} д - да, н - нет  ') == 'д':
                    res1 = ''
                    list_1 = line.split()
                    index_inp = list_1.index(inp)
                    list_1[index_inp] = input("Введите новое значение: ")
                    for i in list_1:
                        res1 += str(i)
                        res1 += ' '
                    res.append(res1 + '\n')
                else:
                    res.append(line)
            else:
                res.append(line)

    with open('file.txt', "w", encoding='utf-8') as file:
        file.writelines(res)


n = int(input("Выберите дествие:\n1 - показать справочник\n2 - добавить абонента\n3 - поиск абонента\n4 - удаление абонента\n5 - изменение абонента\n"))
if n == 1: 
    show_all()
elif n == 2: 
    create_person()
elif n == 3: 
    search()
elif n == 4: 
    delete()
elif n == 5:
    change()