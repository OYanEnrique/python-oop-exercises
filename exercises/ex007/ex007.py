'''
Crie uma classe Livro que vai simular a passagem
de páginas de um livro, considerando também se o
usuário chegou ao fim da leitura
'''
import time
class Livro():
    def __init__(self, livro, paginas):
        self.livro = livro
        self.paginas = paginas
        self.pagina_atual = 0
    def passar_pagina(self, num_paginas):
        for i in range(num_paginas):
            if self.pagina_atual < self.paginas:
                time.sleep(0.1)  # Simula o tempo de leitura de cada página
                print(f'Página {self.pagina_atual + 1} do livro {self.livro}', end='->', flush=True)
                self.pagina_atual += 1
            else:
                print('Você chegou ao fim do livro!')
                break

livro1 = Livro('O Senhor dos Anéis', 10)
livro1.passar_pagina(5)
livro1.passar_pagina(3)
livro1.passar_pagina(4)