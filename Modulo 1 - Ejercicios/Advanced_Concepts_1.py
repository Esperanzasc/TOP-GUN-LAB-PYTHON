class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposito(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Se depositaron {amount} dólares.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retiro(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Se retiraron {amount} dólares.")
            else:
                print(f"Saldo insuficiente para hacer retiro de {amount} dólares.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")
    
    def consultar(self):
        print(f"El saldo actual de la cuenta es: {self.balance} dólares.")


cuenta = BankAccount()  #Se crea instancia de la clase y se asigna a la variable cuenta.
cuenta.consultar()  #Consulta el saldo actual.

cuenta.deposito(250)
cuenta.consultar()  #Consulta el saldo actual.

cuenta.retiro(50)
cuenta.consultar()  #Consulta el saldo actual.

cuenta.retiro(300)  
cuenta.consultar()  # Consulta el saldo actual.
