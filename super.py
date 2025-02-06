class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        pass

    def greet(self):
        print(f"Hello I'm {self.name}")

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Im your student #{self.student_id}")

student1= Student("Juancho",20,"TO1")
student1.greet()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Crear instancias de Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Uso de __str__
print(person1)  # Output: Alice, 30 años

# Uso de __repr__
print(repr(person1))  # Output: Person(name=Alice, age=30)
