from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    """Classe abstrata que define a interface para bebidas quentes"""
    
    def preparar(self):
        """Prepara a bebida quente"""
        pass
    
    def ferver_agua(self):
        """Ferve a água para a bebida quente"""
        print("Água fervida.")
    
    @abstractmethod
    def misturar(self):
        """Mistura os ingredientes da bebida quente"""
        pass
    
    @abstractmethod
    def servir(self):
        """Serve a bebida quente"""
        pass
