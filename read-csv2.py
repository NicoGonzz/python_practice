import csv

file_path = 'products_updated.csv'
updated_file_path = 'modified_products_updated.csv'

products = []
total_general = 0 

with open('products_updated.csv',mode='r') as file:
    csv_reader = csv.DictReader(file)  #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_percentage'] #Pregunta los nombres de las columnas

    for row in csv_reader:
        total_value = float(row['total_value'])  # Extraemos el total_value existente
        products.append(row)
        total_general += total_value  # Sumamos al total general

    with open('modified_products_updated.csv',mode='w',newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames) #Se traen las columnas del anterior archivo
        csv_writer.writeheader() #Escribe el encabezado

        for row in products:  
            percentage = row['total_percentage'] = (float(row['total_value']) / total_general) * 100 if total_general > 0 else 0#Escribimos la fila
            row['total_percentage'] = round(percentage,2)
            csv_writer.writerow(row)
