'''Crie a classe Churrasco, onde seja possível
informar quantas pessoas vão participar 
e mostra quanto de carne deve ser comprado,
o custo total do churrasco e o 
preço por pessoa, 400g por pessoa
e preço 82,40/kg
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

class Churrasco():
    def __init__(self, pessoas):
        self.pessoas = pessoas
    def calcular(self):
        carne = self.pessoas * 0.4
        custo_total = carne * 82.40
        preco_por_pessoa = custo_total / self.pessoas
        return Align.center(Panel(f'[bold cyan]Quantidade de carne:[/bold cyan] {carne:.2f} kg\n[bold cyan]Custo total do churrasco:[/bold cyan] R$ {custo_total:.2f}\n[bold cyan]Preço por pessoa:[/bold cyan] R$ {preco_por_pessoa:.2f}', title='Churrasco', border_style='bold magenta', expand=False))

churrasco1 = Churrasco(4)
print(churrasco1.calcular())
churrasco2 = Churrasco(10)
print(churrasco2.calcular())
