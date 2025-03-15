from collections import deque

def manage_delivery_queue() -> deque:

    delivery_queue = deque(["order 1","order 2", "order 3"])
    delivery_queue.append("order 4") #Agrega al final
    delivery_queue.appendleft("order 0") #Agrega al principio
    delivery_queue.pop() #Elimina el ultimo elemento
    delivery_queue.popleft() #Elimina el primer elemento
    return delivery_queue

queue = manage_delivery_queue()
print(queue)