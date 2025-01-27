#Iterador para numeros impares

#Limite
limit = 20

#Crear el iterador con un rango definido
odd_itter= iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)

#Iterador para numeros pares

#Limite
limit = 20

#Crear el iterador con un rango definido
odd_itter= iter(range(0,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)