from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def verificar_estado_orden(status: OrderStatus):
    if status == OrderStatus.PENDING:
        return "La orden está pendiente."
    elif status == OrderStatus.SHIPPED:
        return "La orden ha sido enviada."
    elif status == OrderStatus.DELIVERED:
        return "La orden ha sido entregada."

estado_actual = OrderStatus.PENDING
print(verificar_estado_orden(estado_actual))  # Output: La orden ha sido enviada.