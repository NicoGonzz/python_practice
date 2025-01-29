#Funciones
def greet(name,last_name="No aplica"):
    print("Hola",name,last_name)

greet("Nicolas","Gonzalez")
greet("Nicolas")
greet(last_name="Juan",name="Marin")

#Calculator
def add(a,b):
    return a+b

def sustract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Seleccione una operacion")
        print("1. Suma") 
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = input("Ingrese su opcion (1,2,3,4,5): ")

        if option =="5":
            print("Ha finalizado la operacion")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option =="1":
                print("La suma es: ", add(num1,num2))
            if option =="2":
                print("La resta es: ", sustract(num1,num2))
            if option =="3":
                print("La multpilicacion es: ", multiply(num1,num2))
            if option =="4":
                print("La division es: ", divide(num1,num2))
        else: 
            print("La opcion en el menu no existe, intente de nuevo")

calculator()
    