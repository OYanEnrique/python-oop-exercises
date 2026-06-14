from personagem import Personagem


class Guerreiro(Personagem):
    """Classe que representa um guerreiro"""
    
    def curar(self):
        """Cura o guerreiro em 10 pontos de vida"""
        self.vida += 10
