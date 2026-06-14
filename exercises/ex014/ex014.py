'''
Simule o sistema de batalha entrepersonagens de um RPG:

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
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
    
    @abstractmethod
    def curar(self):
        pass
    
    def atacar(self, alvo, forca):
        alvo.receber_dano(forca)
    
    def receber_dano(self, dano):
        self.vida -= dano

class Guerreiro(Personagem):
    def curar(self):
        self.vida += 10

class Mago(Personagem):
    def curar(self):
        self.vida += 5
# Exemplo de uso
guerreiro = Guerreiro("Aragorn", 100, ["Corte", "Estocada"])
mago = Mago("Gandalf", 80, ["Bola de Fogo", "Raio"])
guerreiro.atacar(mago, 15)
print(mago.vida)  # Saída: 65
mago.curar()
print(mago.vida)  # Saída: 70