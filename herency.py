class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        pass

    def sell(self):
        if self.is_available:
            self.is_available = False,
            print (f"El vehiculo {self.brand} ha sido vendida")
        else: 
            print (f"El vehiculo {self.brand} no esta disponible")

    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
class Car(Vehicle): #Se hereda la clase
        def start_engine(self):
            if not self.is_available:
                return print(f"El motor del coche {self.brand} esta en marcha")
            else:
                return print("El motor esta apagado")
            
        def stop_engine(self):
            if self.is_available:
                return print(f"El motor del coche {self.brand} esta apagado ")
            else:
                return print(f"El motor del coche {self.brand} esta encendido ")
            
class Bicicle(Vehicle): #Se hereda la clase
        def start_engine(self):
            if not self.is_available:
                return print(f"La bicicleta {self.brand} esta en marcha")
            else:
                return print(f"La bicicleta {self.brand} esta quieta")
            
        def stop_engine(self):
            if self.is_available:
                return print(f"La bicicleta {self.brand} esta quieta ")
            else:
                return print(f"La bicicleta {self.brand} esta  en movimiento ")
            
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []
        pass

    def buy_vehicle(self,vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else: 
            print(f"Lo siento el vehiculo {vehicle.brand} no esta disponible")

    def inquire_vehicle(self,vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
            print(f"El vehiculo {vehicle.brand} está {availability} y cuesta ${vehicle.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        pass

    def add_vehicles(self,vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido agregado al inventario")
        pass

    def register_clients(self,customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} se ha registrado exitosamente")

    def show_available_vehicles(self):
        print(f"Los vehiculos disponibles son:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"Este {vehicle.brand} con valor de {vehicle.get_price()}")

car1 = Car("Susuki","2020",20000)
car2 = Car("Toyota","2014",8000)
bike1 = Bicicle("Text","2018",3000)
bike2 = Bicicle("Go","2000",1300)

customer1 = Customer("Juan Gonzalez")
customer2 = Customer("Nicolas Marin")

dealership = Dealership()
dealership.show_available_vehicles()

dealership.add_vehicles(car1)
dealership.add_vehicles(car2)
dealership.add_vehicles(bike1)
dealership.add_vehicles(bike2)
dealership.show_available_vehicles()

customer1.inquire_vehicle(car1)

customer1.buy_vehicle(car1)

dealership.show_available_vehicles()

dealership.register_clients(customer1)
dealership.register_clients(customer2)

    

            