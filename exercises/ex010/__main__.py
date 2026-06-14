'''Implementação do diagrama de classes
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

from quadrado import Quadrado
from circulo import Circulo


def main():
    """Função principal que executa o programa"""
    # Criando instâncias das classes
    quadrado = Quadrado(5)
    circulo = Circulo(3)
    
    # Exibindo informações do quadrado
    print(f"Quadrado - Lado: {quadrado.lado}")
    print(f"Perímetro: {quadrado.perimetro()}")
    print(f"Área: {quadrado.area()}")
    print(f"Quantidade de lados: {quadrado.qtd_lados}\n")
    
    # Exibindo informações do círculo
    print(f"Círculo - Raio: {circulo.raio}")
    print(f"Perímetro (Circunferência): {circulo.perimetro()}")
    print(f"Área: {circulo.area()}")
    print(f"Quantidade de lados: {circulo.qtd_lados}")


if __name__ == "__main__":
    main()
