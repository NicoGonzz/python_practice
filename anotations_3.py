class Employee:
    name: str
    age: int
    salary: float

    def __init__(self,name: str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary
        pass

    def introduce(self) -> str:
        return f"Hola,me llamo {self.name}, tengo {self.age}"
    
employee1 = Employee('Juan', 22, 1500000.0)
print(employee1.introduce())