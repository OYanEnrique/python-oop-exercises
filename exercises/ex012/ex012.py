'''
Crie uma classe capaz de calcula frete
de veículos diferentes:

*Transporte (abstract)
-distancia
-frete
-calc_frete() (abstract)

*Moto
-fator=0.50
-calc_frete()

*Caminhao
-fator=1.20
-calc_frete() -> min 50km

*Drone
fator=9.50
-calc_frete() -> max 10km
'''
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
    
    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
    
    def calc_frete(self):
        if self.distancia < 50:
            raise ValueError("A distância mínima para caminhão é de 50 km.")
        self.frete = self.distancia * self.fator
        return self.frete

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50
    
    def calc_frete(self):
        if self.distancia > 10:
            raise ValueError("A distância máxima para drone é de 10 km.")
        self.frete = self.distancia * self.fator
        return self.frete

# Exemplo de uso
moto = Moto(20)
print(moto.calc_frete())  # Saída: 10.0
caminhao = Caminhao(50)
print(caminhao.calc_frete())  # Saída: 60.0
drone = Drone(10)
print(drone.calc_frete())  # Saída: 95.0
