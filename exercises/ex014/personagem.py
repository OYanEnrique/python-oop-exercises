from abc import ABC, abstractmethod


class Personagem(ABC):
    """Classe abstrata que define a interface para personagens de RPG"""
    
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
    
    @abstractmethod
    def curar(self):
        """Cura o personagem"""
        pass
    
    def atacar(self, alvo, forca):
        """Ataca um alvo com uma determinada força"""
        alvo.receber_dano(forca)
    
    def receber_dano(self, dano):
        """Recebe dano e reduz a vida"""
        self.vida -= dano
