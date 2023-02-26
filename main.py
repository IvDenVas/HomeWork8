def create_person():
    data = open('file.txt', 'a', encoding='utf-8')
    last_name = input("Введите фамилию: ").title()
    name = input("Введите имя: " ).title()
    patronymic = input("Введите отчество: ").title()
    number = input("Введите номер телефона: ")
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
    res = str(input("Введите поисковые данные: ").title())
    for line in data:
        if res in line.split():
            print(line)
    data.close()
    return print

def delete():
    with open('file.txt', "r",encoding='utf-8') as file:
        temp = file.readlines()
        inp = str(input("Найти и удалить по: ").title())
        res = []
        for line in temp:
            if inp in line and input(f'Эту запись удалить? {line} д - да, н - нет  ') == 'д':
                print(f'Удалено: {line}')
            else:
                res.append(line)

    with open('file.txt', "w", encoding='utf-8') as file:
        file.writelines(res)

def change():
    with open('file.txt', "r", encoding='utf-8') as file:
        temp = file.readlines()
        inp = str(input("Найти и изменить по: ").title())
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
                    print(f'Готово: {line} -> {res1}')
                else:
                    res.append(line)
            else:
                res.append(line)

    with open('file.txt', "w", encoding='utf-8') as file:
        file.writelines(res)

def choose_action():
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

choose_action()
