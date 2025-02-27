from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID en la lista de empleados.

    Parámetros:
    - employee_ids (list[int]): Lista de IDs de empleados disponibles.
    - employee_id (int): ID del empleado a buscar.

    Retorna:
    - Optional[int]: Devuelve el ID si se encuentra en la lista, de lo contrario retorna None.
    """
    # Verifica si el ID del empleado está en la lista
    if employee_id in employee_ids:
        return employee_id  # Retorna el ID si está en la lista
    
    return None  # Retorna None si no se encuentra el ID

# Lista de empleados existentes
employees = [101, 102, 103, 104]

# Buscamos un empleado que existe
found_employee = find_employee(employees, 102)
print(f"Empleado encontrado: {found_employee}")  # ✅ Empleado encontrado: 102

# Buscamos un empleado que NO existe
not_found_employee = find_employee(employees, 200)
print(f"Empleado encontrado: {not_found_employee}")  # ✅ Empleado encontrado: None
