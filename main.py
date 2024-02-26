from csv import reader, writer

# Выполнение 1-й части задания
with open('products.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=',')