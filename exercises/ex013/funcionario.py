from abc import ABC, abstractmethod


class Funcionario(ABC):
    """Classe abstrata que define a interface para funcionários"""
    
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        """Calcula o salário do funcionário"""
        pass
    
    def analisar_sal(self):
        """Analisa se o salário está acima do mínimo"""
        if self.sal_bruto < self.sal_min:
            return f"O salário bruto de {self.nome} é inferior ao salário mínimo."
        else:
            return f"O salário bruto de {self.nome} é superior ou igual ao salário mínimo."
