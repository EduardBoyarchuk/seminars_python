import csv
import view
import database

while True:
    print('1. Добавить контакт')
    print('2. Поиск контакта')
    print('3. Экспорт контактов в txt файл')
    print('4. Сортировка контактов (sort_book.csv)')
    print('5. Вывод списка контактов')
    print('6. Редактирование имени контактов')
    print('7. Удаление контакта')
    print('0. Выход')

    choice = input('Выберите действие: ')

    if choice == '1':
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        middle_name = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        view.add_contact(last_name, first_name, middle_name, phone_number)
    elif choice == '2':
        search_term = input('Введите характеристику поиска: ')
        database.search_contact(search_term)
    elif choice == '3':
        database.export_contacts()
    elif choice == '4':
        database.sorted_contacts_name()
    elif choice == '5':
        database.print_all()
    elif choice == '6':
        name = input('Введите имя для поиска: ')
        new_data = input("Введите новое имя")
        filename = 'phonebook.csv'
        database.edit_contacts(filename, name, new_data)
    elif choice == '7':
        search_term = input('Введите характеристику поиска: ')
        database.del_contact(search_term)
    elif choice == '0':
        break
