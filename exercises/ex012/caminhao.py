from transporte import Transporte


class Caminhao(Transporte):
    """Classe que representa um caminhão para entrega"""
    
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
    
    def calc_frete(self):
        """Calcula o frete do caminhão (mínimo 50 km)"""
        if self.distancia < 50:
            raise ValueError("A distância mínima para caminhão é de 50 km.")
        self.frete = self.distancia * self.fator
        return self.frete
