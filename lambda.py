add = lambda a, b: a + b
print (add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,2))

#Obtener cuadrado de cada numero
numbers = range(100)
squared_numbers = list(map(lambda x: x**2,numbers))
print("Cuadrados:",squared_numbers)

#Numeros pares
even_numbers=list(filter(lambda x: x%2 ==0, numbers))
print("Numeros pares",even_numbers)

#Numeros impares
even_numbers=list(filter(lambda x: x%2 > 0, numbers))
print("Numeros impares",even_numbers)