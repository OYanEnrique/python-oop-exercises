'''Implemente o seguinte diagrama de classes
*Polígono (abstract):
-qtd_lados
-perimetro() (abstract)
-area() (abstract)

*Quadrado
-lado
-perimetro()
-area()

*Circulo
-raio
-perimetro()
-area()
'''
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
    
    def perimetro(self):
        return 2 * 3.14 * self.raio
    
    def area(self):
        return 3.14 * self.raio ** 2

# Exemplo de uso
quadrado = Quadrado(5)
print(quadrado.perimetro())  # Saída: 20
print(quadrado.area())  # Saída: 25

circulo = Circulo(3)
print(circulo.perimetro())  # Saída: 18.84
print(circulo.area())  # Saída: 28.26