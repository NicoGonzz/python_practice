x = 'global' #Variable lobal

#Funcion externa
def outer_function():
    x = 'enclosing'

    #Funcion interna
    def inner_function():
        x = 'local' #Variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)