x= 100

#Variables locales
def local_function():
    x = 10 #Variable local
    print(f"El valor de la variable local es {x}")

def show_variable():
    print(f"El valor de la variable global es {x}")

show_variable()
local_function()
