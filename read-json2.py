import json

file_path = 'products.json'
#Añadir un nuevo producto
new_product = {
    'name': "Computer",
    'price': 720,
    'quantity': 30,
    'brand': "Asus",
    'category': "Electronics",
    'entry_date': '2025/02/13'
}

with open(file_path,mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4) #Añadir informacion con el producto, el nombre y la identacion del json