from personagem import Personagem


class Mago(Personagem):
    """Classe que representa um mago"""
    
    def curar(self):
        """Cura o mago em 5 pontos de vida"""
        self.vida += 5
