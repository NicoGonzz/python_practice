from collections import defaultdict #Defaultdict establece un valor por defecto si no existe uno

def contar_productos(ordenes):
    product_count = defaultdict(int)
    for orden in ordenes:
        product_count[orden] += 1
    return product_count

ordenes = ['laptop', 'smartphone', 'laptop', 'tablet']
resultado = contar_productos(ordenes)
print(resultado)  # Output: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})