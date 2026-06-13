'''
Crie a classe Gamer, onde podemos cadastrar 
nome, nick e os jogos favoritos de uma pessoa.
Crie também um método que permita mostrar a ficha
desse gamer
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

class Gamer():
    def __init__(self, nome, nick, jogos_favoritos):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos

    def ficha(self):
        return Align.center(Panel(f'[bold cyan]Nome:[/bold cyan] {self.nome}\n[bold cyan]Nick:[/bold cyan] {self.nick}\n[bold cyan]Jogos favoritos:[/bold cyan]\n{self.jogos_favoritos}', title='Ficha do gamer', border_style='bold magenta', expand=False))

gamer1 = Gamer('Yan', 'YanEnrique', ['The Last of Us', 'God of War', 'Red Dead Redemption 2'])
print(gamer1.ficha())
