'''
Simule uma cafeteira orientada a objetos:

*Bebida Quente (abstract)
-preparar()
-ferver_agua()
-misturar()
-servir()

*Cafe
-misturar()
-servir()

*Cha
-misturar()
-servir()

*Leite
-misturar()
-servir()
'''
from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    """Classe abstrata que define a interface para bebidas quentes"""
    
    def preparar(self):
        """Prepara a bebida quente"""
        pass
    
    def ferver_agua(self):
        """Ferve a água para a bebida quente"""
        print("Água fervida.")
    
    @abstractmethod
    def misturar(self):
        """Mistura os ingredientes da bebida quente"""
        pass
    
    @abstractmethod
    def servir(self):
        """Serve a bebida quente"""
        pass

class Cafe(BebidaQuente):
    """Classe que representa um café"""
    
    def preparar(self):
        print('Preparando café...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Café preparado.")
    
    def misturar(self):
        print("Café misturado.")
    
    def servir(self):
        print("Café servido.")

class Cha(BebidaQuente):
    """Classe que representa um chá"""
    
    def preparar(self):
        print('Preparando chá...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Chá preparado.")
    
    def misturar(self):
        print("Chá misturado.")
    
    def servir(self):
        print("Chá servido.")

class Leite(BebidaQuente):
    """Classe que representa um leite"""
    
    def preparar(self):
        print('Preparando leite...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Leite preparado.")
    
    def misturar(self):
        print("Leite misturado.")
    
    def servir(self):
        print("Leite servido.")

# Exemplo de uso
cafe = Cafe()
cafe.preparar()
cha = Cha()
cha.preparar()
leite = Leite()
leite.preparar()