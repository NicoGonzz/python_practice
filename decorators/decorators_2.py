def check_access(func):
    def wrapper(employee): #El mismo parametro con otro nombre
        #Validamos el rol de la persona a eliminar
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo el administrador puede eliminar un cliente')
    return wrapper

@check_access
def deleteEmployee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")

admin = {'name': 'Juan', 'role': 'admin'}
employee = {'name': 'Nicolas', 'role': 'employee'}

deleteEmployee(admin)
deleteEmployee(employee)