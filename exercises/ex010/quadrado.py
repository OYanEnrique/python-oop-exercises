from poligono import Poligono


class Quadrado(Poligono):
    """Classe que representa um quadrado"""
    
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    
    def perimetro(self):
        """Calcula o perímetro do quadrado"""
        return self.lado * 4
    
    def area(self):
        """Calcula a área do quadrado"""
        return self.lado ** 2
