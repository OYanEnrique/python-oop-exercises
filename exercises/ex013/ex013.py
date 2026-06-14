'''
Crie a estrutura capaz de calcular salarios de funcionarios diferentes:

*Funcionario (abstract)
-nome
-sal_bruto
-salario
-sal_min =1612
-inss=7.5
-calc_sal() (abstract)
-analisar_sal()

*Horista
-valor_hora
-horas_trab
-calc_sal()

*Mensalista
-calc_sal()
'''

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        pass
        
    def analisar_sal(self):
        if self.sal_bruto < self.sal_min:
            return f"O salário bruto de {self.nome} é inferior ao salário mínimo."
        else:
            return f"O salário bruto de {self.nome} é superior ou igual ao salário mínimo."

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        return self.sal_bruto

class Mensalista(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, 0)
    
    def calc_sal(self):
        self.sal_bruto = 1500
        return self.sal_bruto

# Exemplo de uso
horista = Horista("João", 20, 160)
print(horista.calc_sal())
print(horista.analisar_sal())
mensalista = Mensalista("Maria")
print(mensalista.calc_sal())
print(mensalista.analisar_sal())