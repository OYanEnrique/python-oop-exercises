from bebida_quente import BebidaQuente


class Leite(BebidaQuente):
    """Classe que representa um leite"""
    
    def preparar(self):
        print('Preparando leite...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Leite preparado.")
    
    def misturar(self):
        print("Leite misturado.")
    
    def servir(self):
        print("Leite servido.")
