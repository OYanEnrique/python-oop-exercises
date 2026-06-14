from poligono import Poligono


class Circulo(Poligono):
    """Classe que representa um círculo"""
    
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
    
    def perimetro(self):
        """Calcula o perímetro (circunferência) do círculo"""
        return 2 * 3.14 * self.raio
    
    def area(self):
        """Calcula a área do círculo"""
        return 3.14 * self.raio ** 2
