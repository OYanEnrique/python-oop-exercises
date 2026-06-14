'''Crie a classe Funcionario onde 
podemos cadastrar nome,setor e cargo.
Crie tambem um metodo que permita ao 
funcionario se apresentar
'''
class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentar(self) -> str:
        return f'Olá, meu nome é {self.nome}, trabalho no setor de {self.setor} e meu cargo é {self.cargo}'

funcionario1 = Funcionario('Yan', 'TI', 'Cientista de dados')
print(funcionario1.apresentar())