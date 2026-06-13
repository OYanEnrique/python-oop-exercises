'''
Crie a classe ControleRemoto, onde vamos simular
 o funcionamento de um controle simples 
 (canal, volume e liga/desliga)
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

class ControleRemoto():
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 5

    def __init__(self, canal=1, volume=1):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False
    
    def lig_desliga(self):
        self.ligado = not self.ligado
    
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = 'TV desligada'
        else:
            conteudo = f'CANAL = '


            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[yellow on yellow]{canal}[/]'
                else:
                    conteudo += f'{canal}'

            conteudo += '\nVolume = '
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'
        
        tv = Panel(conteudo, title='TV', width = 30)
        print(tv)

controle1 = ControleRemoto()
while True:
    controle1.mostrar_tv()
    comando = input('Digite um comando (L - ligar/desligar, C+ - canal mais, C- - canal menos, V+ - volume mais, V- - volume menos): ').upper()
    if comando == 'L':
        controle1.lig_desliga()
    elif comando == 'C+':
        controle1.canal_mais()
    elif comando == 'C-':
        controle1.canal_menos()
    elif comando == 'V+':
        controle1.volume_mais()
    elif comando == 'V-':
        controle1.volume_menos()
    else:
        print('Comando inválido')
        break
    print('\n' * 10)