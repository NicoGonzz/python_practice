#Leer archivo linea por linea
"""with open('prince.txt','r') as file:
    for lines in file:
        # Leemos cada línea y eliminamos los saltos de línea al final
        print("Leyendo linea:",lines.strip())"""

#Leer todas las lineas en una lista y muestra los saltos de linea
"""with open('prince.txt','r') as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto con A
"""with open('prince.txt','a') as file:
    file.write("\n\nBy:Nicolas Gonzalez.")"""

#Sobreescribir el texto completo con el cambio a W
"""with open('prince.txt','w') as file:
    file.write("\n\nBy:Nicolas Gonzalez.")"""

#Contar lineas
with open('prince.txt','r') as file:
    lines = file.readlines()
    print(len(lines))
