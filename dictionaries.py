numbers = {1:"uno", 2:"dos",3:"tres"} #Clase diccionario
print(numbers)
print(type(numbers))
print(numbers[1])
information ={"nombre":"Juan",
              "pais": "Colombia",
              "Altura": 1.80,
              "Edad": 20}
print(information)
del information["Edad"]
print(information)
claves = information.keys() # Claves del diccionario
print(claves)
#print(type(claves))
values = information.values() # Valores del diccionario
print(values)

contactos = {
    "Juan": {
        "pais": "Colombia",
        "Altura": 1.80,
        "Edad": 20
    },
    "Camilo": {
        "pais": "Colombia",
        "Altura": 1.70,
        "Edad": 23
    },
    "Natalia": {
        "pais": "Colombia",
        "Altura": 1.65,
        "Edad": 22
    }
}

print(contactos["Juan"])

