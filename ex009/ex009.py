'''
Crie a classe Caneta, que simula o funcionamento 
de uma caneta colorida, podendo escrever frases
na cor relativa
'''
from rich import print

class Caneta():
    def __init__(self):
        self.esta_destampada = False
        self.cor = ''
    
    def destampar(self):
        self.esta_destampada = True
        return 'Caneta destampada, agora você pode escrever'
    
    def tampar(self):
        self.esta_destampada = False
        return 'Caneta tampada, agora você não pode escrever'
        
    def escrever(self, cor, frase=''):
        self.cor = cor
        return f'[bold {cor}]{frase}[/bold {cor}]' if self.esta_destampada else f'[bold red]A caneta está tampada, destampe para escrever[/bold red]'

caneta1 = Caneta()
print(caneta1.destampar())
print(caneta1.escrever('blue', 'Olá, mundo!'))
print(caneta1.tampar())
print(caneta1.destampar())
print(caneta1.tampar())
print(caneta1.escrever('blue', 'Olá, mundo!'))