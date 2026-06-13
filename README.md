# Python OOP Exercises 🐍

Repositório de exercícios práticos de Programação Orientada a Objetos em Python, abordando conceitos fundamentais como classes, herança, polimorfismo, encapsulamento e abstração.

## 📋 Sobre

Este repositório contém uma coleção de exercícios desenvolvidos para praticar e consolidar conhecimentos em POO (Programação Orientada a Objetos) utilizando Python. Cada exercício está organizado em seu próprio diretório com exemplos práticos e documentados.

## 🎯 Objetivos

- Praticar conceitos fundamentais de Programação Orientada a Objetos
- Desenvolver habilidades em design de classes e objetos
- Aplicar os pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo
- Criar código limpo, organizado e seguindo boas práticas

## 📚 Exercícios

### ex001 - Fazendo Bolinhos
Exercício introdutório sobre classes e objetos em Python. Demonstra:
- Criação de classes simples
- Uso de construtores (`__init__`)
- Atributos de instância
- Métodos de instância
- Validação de condições

**Conceitos abordados:**
- Classes e objetos
- Atributos booleanos
- Métodos com lógica condicional
- Instanciação de múltiplos objetos

### ex002 - Conta Bancária
Sistema básico de conta bancária demonstrando operações fundamentais. Implementa:
- Geração automática de IDs únicos com UUID
- Operações bancárias (depósito e saque)
- Validação de saldo
- Método `__str__` para representação de objetos
- Parâmetros opcionais com valores padrão

**Conceitos abordados:**
- Uso do módulo `uuid` para identificadores únicos
- Métodos especiais (`__init__`, `__str__`)
- Encapsulamento de lógica de negócio
- Validação de operações
- Formatação de valores monetários

### ex003 - Funcionário
Sistema de cadastro de funcionários com apresentação. Demonstra:
- Criação de classes com múltiplos atributos
- Método de apresentação e comunicação
- Uso de f-strings para formatação

**Conceitos abordados:**
- Atributos de instância
- Métodos de comunicação
- Type hints para retorno de valores
- Estruturação básica de classes

### ex004 - Produto
Sistema de gestão de produtos com exibição visual de etiquetas de preço. Implementa:
- Armazenamento de informações de produto (nome e preço)
- Método para gerar etiquetas formatadas
- Integração com biblioteca `rich` para formatação visual

**Conceitos abordados:**
- Métodos de retorno de dados formatados
- Integração com bibliotecas externas
- Apresentação visual de dados
- Formatação de valores monetários

### ex005 - Churrasco
Calculadora para churrasco que determina quantidade de carne e custos. Calcula:
- Quantidade total de carne necessária (400g por pessoa)
- Custo total do churrasco (R$ 82,40/kg)
- Preço individual por pessoa
- Apresentação visual dos resultados

**Conceitos abordados:**
- Métodos com cálculos matemáticos
- Formatação de valores numéricos
- Lógica de negócio
- Apresentação formatada com `rich`

### ex006 - Controle Remoto
Simulação completa de um controle remoto com funcionalidades de TV. Implementa:
- Atributos de classe para limites (canal e volume)
- Controle de ligado/desligado
- Navegação entre canais (com ciclo)
- Controle de volume com limites
- Validação de estado (TV deve estar ligada)

**Conceitos abordados:**
- Atributos de classe vs. instância
- Métodos que modificam estado
- Lógica condicional complexa
- Encapsulamento de regras de negócio

### ex007 - Livro
Simulador de passagem de páginas de um livro interativo. Recursos:
- Rastreamento de páginas lidas
- Simulação de tempo de leitura
- Detecção de fim de livro
- Passagem múltipla de páginas

**Conceitos abordados:**
- Controle de estado do objeto
- Loops e condicionais
- Uso do módulo `time`
- Incremento progressivo de atributos

### ex008 - Gamer
Ficha de perfil de jogador com informações e preferências. Contém:
- Informações pessoais (nome e nick)
- Lista de jogos favoritos
- Método para exibir ficha formatada

**Conceitos abordados:**
- Trabalhar com coleções (listas)
- Atributos complexos
- Formatação visual de dados
- Representação de objetos complexos

### ex009 - Caneta
Simulação de uma caneta colorida com estados e funcionalidades. Implementa:
- Estado de tampada/destampada
- Validação de estado antes de escrever
- Escrita colorida com formatação
- Feedback de operações

**Conceitos abordados:**
- Estados de objeto (booleano)
- Validação antes de operações
- Métodos que retornam mensagens
- Uso de valor padrão em parâmetros
- Integração com `rich` para cores

## 🚀 Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/OYanEnrique/python-oop-exercises.git
```

2. Navegue até o diretório do exercício desejado:
```bash
cd python-oop-exercises/ex001
```

3. Execute o arquivo Python:
```bash
python ex001.py
```

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Conhecimentos básicos de Python

## 🛠️ Tecnologias

- Python 3.x

## 📖 Estrutura do Projeto

```
python-oop-exercises/
│
├── README.md
│
├── ex001/
│   └── ex001.py
│
├── ex002/
│   └── ex002.py
│
├── ex003/
│   └── ex003.py
│
├── ex004/
│   └── ex004.py
│
├── ex005/
│   └── ex005.py
│
├── ex006/
│   └── ex006.py
│
├── ex007/
│   └── ex007.py
│
├── ex008/
│   └── ex008.py
│
└── ex009/
    └── ex009.py
```

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com novos exercícios ou melhorias! 

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovoExercicio`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo exercício'`)
4. Push para a branch (`git push origin feature/NovoExercicio`)
5. Abra um Pull Request

<div align="center">

<br>

**Autor do Projeto:** [Yan Enrique (OYanEnrique)](https://github.com/OYanEnrique)  
*(Cientista de Dados | Engenheiro de Machine Learning)*

</div>

---

## 📝 Licença

This project is licensed under the **MIT**. See the [LICENSE](LICENSE) for more details.