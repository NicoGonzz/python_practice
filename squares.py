numbers = [1,2,3,4,5]

squares = []

for number in numbers:
    square = number **2
    squares.append(square)

print(squares)

#Optimizado
squares3 = [x**3 for x in numbers]
print(squares3)
    