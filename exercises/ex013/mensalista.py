from funcionario import Funcionario


class Mensalista(Funcionario):
    """Classe que representa um funcionário mensalista"""
    
    def __init__(self, nome):
        super().__init__(nome, 1500)
    
    def calc_sal(self):
        """Calcula o salário do mensalista"""
        return self.sal_bruto
