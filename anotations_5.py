from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Convierte un salario en un número de tipo float.

    Parámetros:
    - salary (Union[int, float]): El salario a procesar. Puede ser un entero o un número decimal.

    Retorna:
    - float: El salario convertido a tipo flotante.
    """
    return float(salary)  # Convierte el salario a float y lo devuelve

# 🔹 Ejemplo de uso:
salary_int = 5000  # Salario como entero
salary_float = 7500.50  # Salario como flotante

# Procesamos los salarios
print(f"Salario procesado (int): {process_salary(salary_int)}")  # ✅ Salida: 5000.0
print(f"Salario procesado (float): {process_salary(salary_float)}")  # ✅ Salida: 7500.5
