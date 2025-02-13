import json

#Lectura del archivo
with open('products.json', mode='r') as file:
    products = json.load(file)

#Mostrar contenido
for product in products:
    print(f"Producto: {product['name']},Price: {product['price']}") #Solo imprimimos un dato