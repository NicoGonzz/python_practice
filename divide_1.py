def divide(a: int, b: int ) -> float:
    #Validamos los parametros para ver si son enteros
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Ambos parametros deben ser enteros.')
        #print(f"Error: Ambos parametros deben ser enteros o flotantes")
        #return None
    #Verificamos que el divisior no sea 0
    if b == 0:
        raise ZeroDivisionError('El divisor no puede ser 0')
        #print(f"Error: El divisior no puede ser 0")
        #return None
    return a/b

#Ejemplos de uso
try:
    res = divide(10,4) #Error de tipo
    print(res)
except (ZeroDivisionError,TypeError) as e:
    print(f'Error: {e}')
 