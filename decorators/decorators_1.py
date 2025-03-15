def log_transaction(func):
    def wrapper(): #Envuelve la funcion
        print('1. Log de la transaccion ...')
        func()
        print('3. Log terminado ...')
    return wrapper

@log_transaction #Usamos el decorador
def process_payment():
    print('2. Procesando Pagos .....')

process_payment()