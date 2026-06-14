'''Simule uma cafeteira orientada a objetos:

*Bebida Quente (abstract)
-preparar()
-ferver_agua()
-misturar()
-servir()

*Cafe
-misturar()
-servir()

*Cha
-misturar()
-servir()

*Leite
-misturar()
-servir()
'''

from cafe import Cafe
from cha import Cha
from leite import Leite


def main():
    """Função principal que executa o programa"""
    cafe = Cafe()
    cafe.preparar()
    
    cha = Cha()
    cha.preparar()
    
    leite = Leite()
    leite.preparar()


if __name__ == "__main__":
    main()
