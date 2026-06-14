from transporte import Transporte


class Drone(Transporte):
    """Classe que representa um drone para entrega"""
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50
    
    def calc_frete(self):
        """Calcula o frete do drone (máximo 10 km)"""
        if self.distancia > 10:
            raise ValueError("A distância máxima para drone é de 10 km.")
        self.frete = self.distancia * self.fator
        return self.frete
