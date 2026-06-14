import uuid
class ContaBancaria:
    """
    Cria uma conta bancária com funcionalidades básicas.
    """
    def __init__(self, nome, saldo=0.0, id=None):
        self.id = str(uuid.uuid4()) if id is None else id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"ContaBancaria(ID: {self.id}, Nome: {self.nome}, Saldo: R${self.saldo:,.2f})"

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:,.2f} realizado com sucesso!"

    def saque(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente!"
        self.saldo -= valor
        return f"Saque de R${valor:,.2f} realizado com sucesso!"
        
yan_enrique = ContaBancaria("Yan Enrique", 1000.0)
print(yan_enrique)
print(yan_enrique.deposito(500.0))
print(yan_enrique.saque(100000.0))
print(yan_enrique)