class BankAccount:
    def __init__(self,account_holder,balance,account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number
        self.is_active = True
        pass

    def deposit(self,amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo Actual {self.balance}")
        else:
           print(f"La cuenta {self.account_number} esta inactiva")

    def withdraw(self,amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo Actual {self.balance}")
        else:
           print(f"La cuenta {self.account_number} esta inactiva")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta {self.account_number} ha sido deshabilitada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta {self.account_number} ha sido habilitada")

account1 = BankAccount("Juan",1000,987654321)
account2 = BankAccount("Nicolas",8000,984722323)
account3 = BankAccount("Natalia",1000,123456789)

#Llamada a los metodos
account1.deposit(300)
account2.withdraw(2000)
account3.deactivate_account()
account3.deposit(1000)



