from abc import ABC, abstractmethod


class Transporte(ABC):
    """Classe abstrata que define a interface para transportes"""
    
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        """Calcula o frete para o transporte"""
        pass
