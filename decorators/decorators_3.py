#Decorador que valida si un empleado tiene un rol especifico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Validamos si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print('ACCESO DENEGADO. Solo el administrador puede eliminar un cliente')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion de {employee["name"]} en el log')
        return func(employee)
    return wrapper



@check_access('admin')
@log_action #Regisramos la accion en un log
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")

admin = {'name': 'Juan', 'role': 'admin'}
employee = {'name': 'Nicolas', 'role': 'employee'}

delete_employee(admin)
#delete_employee(employee)