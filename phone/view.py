import controller
def menu():
    print('''Меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Создать контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить контакт
        8. Выход''')
    choise = int(input("Выберите пункт меню: "))
    return choise

def show_contact(pb: list[dict]):
    if pb == []:
        print("Телефонная книга пуста")
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {phone:<15} {comment:<20}')

def new_contact_input():
    name = input("Введите имя и фамилию: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    new_contact = {}
    new_contact["name"] = name
    new_contact["phone"] = phone
    new_contact["comment"] = comment
    return new_contact

def find_contact():
    find = input("Введите элемент для поиска: ")
    return find

def input_id():
    ind = int(input("Введите индекс "))
    return ind
