from bebida_quente import BebidaQuente


class Cafe(BebidaQuente):
    """Classe que representa um café"""
    
    def preparar(self):
        print('Preparando café...')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Café preparado.")
    
    def misturar(self):
        print("Café misturado.")
    
    def servir(self):
        print("Café servido.")
