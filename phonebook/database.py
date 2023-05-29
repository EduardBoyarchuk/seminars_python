from csv import *
from view import *


def search_contact(search_term):
    with open('phonebook.csv', mode='r') as file:
        readers = csv.reader(file)
        for row in readers:
            if search_term in row:
                print(row)


def export_contacts():
    with open('phonebook.csv', mode='r') as file:
        readers = csv.reader(file)
        with open('phonebook.txt', mode='w') as export_file:
            for row in readers:
                export_file.write(','.join(row) + '\n')


def sorted_contacts_name():
    a = int(input(print('Как сортировать справочник введите номер:',
                        '1 - По фамилии',
                        '2 - По имени',
                        '3 - По отчеству',
                        '4 - По номеру телефона')))
    with open('phonebook.csv', mode='r') as file:
        reader = csv.reader(file)
        sorted_reader = sorted(reader, key=lambda row: row[a-1])

    with open('sorted_file.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_reader)

def print_all():
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def del_contact(search_term):
    with open('phonebook.csv', mode='r') as file:
        readers = csv.reader(file)
        with open('new_file.csv', 'w', newline='') as new_file:
            writer = csv.writer(new_file)
            for row in readers:
                if search_term not in row:
                    writer.writerow(row)
    with open('phonebook.csv', mode='w', newline='') as csv_file:
        with open('new_file.csv', mode='r') as temp_file:
            csv_file.write(temp_file.read())
    print_all()


# def edit_contacts(search_term):
#     pass


def edit_contacts(filename, name, new_data):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            if row[1] == name:
                row[1] = new_data

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



#
# def edit_record(filename, name, new_data):
#     rows = []
#     with open(filename, 'r', newline='') as file:
#         reader = csv.DictReader(file)
#         fieldnames = reader.fieldnames
#         for row in reader:
#             if row['имя'] == name:
#                 row.update(new_data)
#             rows.append(row)
#
#     with open(filename, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)
#
# # Пример использования функции edit_record
# name_to_edit = 'Иван'
# new_data = {'фамилия
