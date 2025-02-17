import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['Verde','Azul','Rojo','Amarillo']
random_colors = random.choice(colors)
print("El color es:", random_colors)

#Barajar lista de cartas
cards = ['As','Rey','Reina','Jota','10']
random.shuffle(cards)
print(cards)
