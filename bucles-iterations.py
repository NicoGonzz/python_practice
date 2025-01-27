#Iteramos el array de numeros
numbers = [1,2,3,4,5,6]
for i in numbers:
        print("I es igual a:",i)

#Empezamos desde el rango 3 hasta el 10
for i in range(3,10):
    print(i)

#Iteracion de frutas
fruits = ["Manzana","Pera","Guayaba","Uva","Mango","Banano","Ciruela","Papaya"]
for fruit in fruits: 
    print(fruits)
    if fruit == "Pera":
         print("Esta es una pera")

#Prueba de While
x = 0
while x<5:
     if x==4:
          print("Se acabo la iteracion")
          break
     print(x)
     x +=1

#Prueba de While
x = 10
while x>5:
     if x==6:
          print("Se acabo la iteracion")
          break
     elif x==3:
          print("Se acabo")
          break
print(x)
x +=1

#Iteramos el array de numeros
numbers = [1,2,3,4,5,6]
for i in numbers:
        if i==3 or i==5:
              continue
        print("I es igual a:",i)