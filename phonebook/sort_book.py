import csv

with open('phonebook.csv', 'r') as f:
    reader = csv.reader(f)
    sorted_reader = sorted(reader, key=lambda row: row[0])

with open('sorted_file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sorted_reader)
