import csv


def add_contact(last_name, first_name, middle_name, phone_number):
    with open('phonebook.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([last_name, first_name, middle_name, phone_number])
