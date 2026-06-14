from transporte import Transporte


class Moto(Transporte):
    """Classe que representa uma moto para entrega"""
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
    
    def calc_frete(self):
        """Calcula o frete da moto"""
        self.frete = self.distancia * self.fator
        return self.frete
