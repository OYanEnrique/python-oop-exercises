'''Crie a estrutura capaz de calcular salários de funcionários diferentes:

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

from horista import Horista
from mensalista import Mensalista


def main():
    """Função principal que executa o programa"""
    horista = Horista("João", 20, 160)
    horista.calc_sal()
    print(f"Horista - {horista.nome}: R$ {horista.sal_bruto:.2f}")
    print(horista.analisar_sal())
    
    mensalista = Mensalista("Maria")
    mensalista.calc_sal()
    print(f"\nMensalista - {mensalista.nome}: R$ {mensalista.sal_bruto:.2f}")
    print(mensalista.analisar_sal())


if __name__ == "__main__":
    main()
