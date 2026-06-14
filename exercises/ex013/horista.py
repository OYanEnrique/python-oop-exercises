from funcionario import Funcionario


class Horista(Funcionario):
    """Classe que representa um funcionário horista"""
    
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def calc_sal(self):
        """Calcula o salário do horista"""
        self.sal_bruto = self.valor_hora * self.horas_trab
        return self.sal_bruto
