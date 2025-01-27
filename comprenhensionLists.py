#Numeros cuadrados
squares = [x**2 for x in range(1,11)]
print("Cuadrados",squares)

#Celsius a farenheit
celsius = [0,10,24,32,40]
farenheit = [(temp * 9/5)*32 for temp in celsius]
print("Temperatura en Farenheit",farenheit)

#Numeros pares y impares
evens = [x for x in range(1,21) if x%2 == 0]
print("Numeros pares",evens)
evens = [x for x in range(1,21) if x%2 != 0]
print("Numeros impares",evens)

#Matriz
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print("Matriz normal",matrix)
print("Transpuesta",transposed)