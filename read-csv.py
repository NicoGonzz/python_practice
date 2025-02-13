import csv

#Leer un archivo 
"""with open('products_updated.csv',mode ='r') as file:
    csv_reader = csv.DictReader(file) # Formato de diccionario
    for row in csv_reader: #Itera por filas y la llave es el nombre de la columna
        print(row)  """

#Mostrar la informacion por columnas especificas
"""with open('products_updated.csv',mode ='r') as file:
    csv_reader = csv.DictReader(file) 
    for row in csv_reader:
        print(f"Producto: {row['name']},Precio: {row['price']}")"""

#Añadir un nuevo producto
new_product = {
    'name': "Computer",
    'price': 720,
    'quantity': 30,
    'brand': "Asus",
    'category': "Electronics",
    'entry_date': '2025/02/13'
}

with open('products_updated.csv',mode='a',newline='') as file:
    file.write('\n') #Da un salto de linea para no escribir sobre otra fila
    csv.writer = csv. DictWriter(file, fieldnames= new_product.keys()) #Modo escritura del archivo
    csv.writer.writerow(new_product) #Se escribe en una fila el producto