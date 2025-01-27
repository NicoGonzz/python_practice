#Condicionales
x=50
if x > 5:
    print("X es mayor que 5")
elif x==5:
    print("X es igual a 5")
else:
    print("X no es mayor que 5")
print("Ya se acabo la iteracion")

#Condicionales parte 2 
x1=9
y1=14
if x1>10 and y1>15:
    print("Los numeros son mayores")
if x1>10 or y1>15:
    print("Uno de los dos numeros es mayor")
if not x1>10 and not y1>15:
    print("Ninguno de los resultados es mayor a los propuestos")
    
#Ejemplo condicionales 
is_member = True
age=15
if is_member:
        if age >= 15:
            print("Tienes acceso")
        else:
            print("No tienes acceso debes tener mas de 14 años para tener acceso")
else: 
    print("No eres miembro y no tienes acceso") 