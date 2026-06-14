from abc import ABC, abstractmethod


class Poligono(ABC):
    """Classe abstrata que define a interface para polígonos"""
    
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        """Calcula o perímetro do polígono"""
        pass
    
    @abstractmethod
    def area(self):
        """Calcula a área do polígono"""
        pass
