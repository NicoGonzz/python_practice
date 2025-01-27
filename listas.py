to_do = ["Dirigirnos al hotel",
         "Comer en el hotel",
         "Nadar en el mar",
         "Tomar en el bar",
         "Dormir en el hotel"]

print(to_do)

numbers = [1,2,3,4,5,6,7]
print(type(numbers))
mix = ["uno",2,3,4.12,True,[1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento",mix[0])
print("Ultimo elemento",mix[-1])
print(mix[:2]) #Busca hasta la segunda posicion
print(mix[2:]) #Busca desde la segunda hasta la final
mix.append(False) #Se agrega
print(mix)
mix.insert(1,["a","b"]) #Se agregan datos a la posicion indicada
print(mix) 
print(mix.index(["a","b"]))#Da la posicion de  los datos
print(max(numbers)) #Devuelve el numero mayor
print(min(numbers)) #Devuelve el numero menor del arreglo
del numbers[-1] #Elimina un elemento en especifico
del mix[:2] #Elimina datos hasta la segunda posicion
