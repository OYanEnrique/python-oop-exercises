'''Crie a classe produto, onde podemos cadastrar
nome e o preço. Crie também um método que mostre
uma etiqueta de preço do produto
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Align.center(Panel(f'[bold cyan]{'Preço:'}[/bold cyan]\n[green]R$ {self.preco:.2f}[/green]', title=self.nome, border_style='bold magenta', expand=False))
        
produto1 = Produto('Nintendo Switch 2', 3200.00)
print(produto1.etiqueta())