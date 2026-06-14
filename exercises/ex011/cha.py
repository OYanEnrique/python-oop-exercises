from bebida_quente import BebidaQuente


class Cha(BebidaQuente):
    """Classe que representa um chá"""
    
    def preparar(self):
        print('Preparando chá...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Chá preparado.")
    
    def misturar(self):
        print("Chá misturado.")
    
    def servir(self):
        print("Chá servido.")
