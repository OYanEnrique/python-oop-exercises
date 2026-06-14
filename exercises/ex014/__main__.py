'''Simule o sistema de batalha entre personagens de um RPG:

*Personagem (abstract)
-nome
-vida
-golpes
-atacar(alvo,forca)
-receber_dano(dano)
-curar() (abstract)

*Guerreiro
-curar()

*Mago
-curar()
'''

from guerreiro import Guerreiro
from mago import Mago


def main():
    """Função principal que executa o programa"""
    guerreiro = Guerreiro("Aragorn", 100, ["Corte", "Estocada"])
    mago = Mago("Gandalf", 80, ["Bola de Fogo", "Raio"])
    
    print(f"Vida inicial - Guerreiro: {guerreiro.vida}, Mago: {mago.vida}")
    
    guerreiro.atacar(mago, 15)
    print(f"Após ataque do guerreiro - Vida do mago: {mago.vida}")
    
    mago.curar()
    print(f"Após cura do mago - Vida do mago: {mago.vida}")


if __name__ == "__main__":
    main()
