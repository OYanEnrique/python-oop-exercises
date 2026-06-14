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

### ex010 - Polígonos (Classes Abstratas)
Sistema de cálculo de perímetro e área para diferentes polígonos. Implementa:
- Classe abstrata `Poligono` com métodos abstratos
- Classe `Quadrado` com cálculos de perímetro e área
- Classe `Circulo` com cálculos de circunferência e área
- Estrutura modularizada com separação de responsabilidades

**Conceitos abordados:**
- Classes abstratas e métodos abstratos (`ABC`, `@abstractmethod`)
- Herança de classes abstratas
- Implementação de contratos de interface
- Atributos de classe
- Modularização de código

### ex011 - Cafeteria (Template Method)
Simulação de uma máquina de café com diferentes bebidas quentes. Implementa:
- Classe abstrata `BebidaQuente` com template method
- Diferentes tipos de bebidas: Café, Chá, Leite
- Processo padrão de preparação (fervir água, misturar, servir)
- Customização por subclasses

**Conceitos abordados:**
- Padrão Template Method
- Métodos concretos e abstratos em uma classe abstrata
- Polimorfismo em ação
- Reutilização de código comum
- Modularização com múltiplos arquivos

### ex012 - Transportes (Frete)
Sistema de cálculo de frete para diferentes tipos de transporte. Implementa:
- Classe abstrata `Transporte` com método abstrato `calc_frete()`
- Diferentes transportes: Moto, Caminhão, Drone
- Validações específicas por tipo (distância mínima/máxima)
- Cálculo de frete com fatores diferentes

**Conceitos abordados:**
- Validação de restrições por tipo
- Tratamento de exceções (`ValueError`)
- Fatores e cálculos específicos
- Padrão polimórfico
- Modularização com separação de classes

### ex013 - Funcionários (Polimorfismo)
Sistema de cálculo de salários para diferentes tipos de funcionários. Implementa:
- Classe abstrata `Funcionario` com método `analisar_sal()`
- Tipos: Horista (calcula por horas) e Mensalista
- Validação de salário mínimo
- Constantes de classe (sal_min, inss)

**Conceitos abordados:**
- Polimorfismo em cálculos de salário
- Atributos com valores padrão
- Análise de dados (comparação com mínimo)
- Herança com inicialização diferente
- Métodos concretos na classe abstrata

### ex014 - RPG (Sistema de Batalha)
Sistema de batalha para um RPG com diferentes tipos de personagens. Implementa:
- Classe abstrata `Personagem` com métodos de ataque e cura
- Tipos: Guerreiro (cura 10 pontos) e Mago (cura 5 pontos)
- Sistema de dano e vida
- Interação entre personagens (atacar, receber dano, curar)

**Conceitos abordados:**
- Simulação de comportamentos interativos
- Polimorfismo em métodos de cura
- Gestão de estado (vida)
- Métodos que afetam outros objetos
- Modularização de lógica de jogo

## 🚀 Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/OYanEnrique/python-oop-exercises.git
```

2. Navegue até o diretório do exercício desejado:
```bash
cd python-oop-exercises/exercises/ex001
```

3. Execute o arquivo Python:

Para exercícios simples (ex001-ex009):
```bash
python ex00X.py
```

Para exercícios modularizados (ex010+):
```bash
python __main__.py
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
├── exercises/
│   ├── ex001/
│   │   └── ex001.py
│   │
│   ├── ex002/
│   │   └── ex002.py
│   │
│   ├── ex003/
│   │   └── ex003.py
│   │
│   ├── ex004/
│   │   └── ex004.py
│   │
│   ├── ex005/
│   │   └── ex005.py
│   │
│   ├── ex006/
│   │   └── ex006.py
│   │
│   ├── ex007/
│   │   └── ex007.py
│   │
│   ├── ex008/
│   │   └── ex008.py
│   │
│   ├── ex009/
│   │   └── ex009.py
│   │
│   ├── ex010/
│   │   ├── __main__.py
│   │   ├── poligono.py
│   │   ├── quadrado.py
│   │   └── circulo.py
│   │
│   ├── ex011/
│   │   ├── __main__.py
│   │   ├── bebida_quente.py
│   │   ├── cafe.py
│   │   ├── cha.py
│   │   └── leite.py
│   │
│   ├── ex012/
│   │   ├── __main__.py
│   │   ├── transporte.py
│   │   ├── moto.py
│   │   ├── caminhao.py
│   │   └── drone.py
│   │
│   ├── ex013/
│   │   ├── __main__.py
│   │   ├── funcionario.py
│   │   ├── horista.py
│   │   └── mensalista.py
│   │
│   └── ex014/
│       ├── __main__.py
│       ├── personagem.py
│       ├── guerreiro.py
│       └── mago.py
│
└── LICENSE
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