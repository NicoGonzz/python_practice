#Programacion orientada a objetos
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Person("Ana",30)
person2 = Person("Juan",22)

person1.greet()
person2.greet()