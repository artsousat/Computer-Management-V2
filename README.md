# Computer Management — V2

Sistema de gerenciamento de equipamentos desenvolvido em **Python**, criado para controlar professores, dispositivos, estoque, empréstimos e devoluções em um ambiente escolar.

A V2 representa a evolução do projeto inicial, introduzindo **persistência de dados em JSON**, organização do código em módulos, controle de estoque, histórico de movimentações e uma estrutura preparada para futuras versões com **SQLite, SQL e modelagem de banco de dados**.

## Objetivo

O projeto simula um sistema utilizado para controlar equipamentos de uma escola, permitindo acompanhar quais dispositivos estão disponíveis, emprestados, quebrados ou desaparecidos.

Além de desenvolver conhecimentos em Python, o projeto foi construído pensando na evolução dos dados gerados pelo sistema, que futuramente serão utilizados em uma estrutura de banco de dados e consultas SQL.

## Funcionalidades

### Professores

* Cadastro de professores
* Visualização dos professores cadastrados
* Remoção de professores
* Identificação por ID
* Persistência dos dados em JSON

### Dispositivos

* Cadastro de dispositivos
* Visualização dos dispositivos
* Remoção de dispositivos
* Controle de estoque
* Controle de dispositivos disponíveis
* Registro de dispositivos quebrados
* Registro de dispositivos desaparecidos
* Registro de dispositivos encontrados
* Registro de dispositivos consertados

### Empréstimos

* Registro de empréstimos
* Associação entre professor e dispositivo
* Controle da quantidade emprestada
* Atualização do estoque disponível
* Identificação dos empréstimos por ID
* Registro de data e horário
* Visualização dos empréstimos ativos
* Devolução total
* Devolução parcial

### Histórico

* Registro das devoluções
* Armazenamento das informações do empréstimo
* Registro da data de devolução
* Histórico persistente em JSON
* Opção de limpeza do histórico

## Tecnologias utilizadas

* **Python**
* **JSON**
* **Git / GitHub**
* Estruturas de dados
* Funções
* Condicionais
* Laços de repetição
* Manipulação de arquivos
* Organização modular

## Estrutura do projeto

```text
Computer Management-V2/
│
├── dados/
│   ├── professores.json
│   ├── dispositivos.json
│   ├── emprestimos.json
│   └── historico.json
│
├── src/
│   ├── professores.py
│   ├── dispositivos.py
│   ├── emprestimos.py
│   └── utils.py
│
├── main.py
└── README.md
```

## Organização

O projeto foi dividido em módulos para separar as responsabilidades do sistema:

* `main.py` → menu principal e inicialização
* `professores.py` → gerenciamento dos professores
* `dispositivos.py` → gerenciamento dos equipamentos e estoque
* `emprestimos.py` → empréstimos, devoluções e histórico
* `utils.py` → funções utilizadas em diferentes partes do sistema
* `dados/` → armazenamento persistente das informações

Essa organização permite que cada parte do sistema seja desenvolvida e modificada separadamente.

## Persistência de dados

Na V2, os dados deixam de existir apenas durante a execução do programa.

As informações são armazenadas em arquivos `.json`, permitindo que o sistema seja fechado e executado novamente sem perder os dados cadastrados.

Os principais arquivos são:

```text
professores.json
dispositivos.json
emprestimos.json
historico.json
```

A persistência também prepara o projeto para uma próxima etapa: substituir os arquivos JSON por um **banco de dados relacional**.

## Evolução do projeto

O Computer Management está sendo desenvolvido por versões, acompanhando a evolução dos conhecimentos utilizados no projeto.

```text
V1
Python + lógica de programação
        ↓
V2
Python + módulos + persistência + JSON
        ↓
Próxima etapa
SQLite + SQL + modelagem de dados
        ↓
Futuras versões
Banco de dados + consultas + métricas + análise
```

A ideia é utilizar o mesmo cenário como base para estudar diferentes conceitos de desenvolvimento e, principalmente, de **Engenharia de Dados**.

## Conhecimentos desenvolvidos

Durante o desenvolvimento da V2 foram praticados:

* lógica de programação;
* criação e utilização de funções;
* estruturas condicionais;
* estruturas de repetição;
* listas e dicionários;
* manipulação de arquivos;
* leitura e escrita de JSON;
* tratamento de erros;
* organização de projetos Python;
* divisão do sistema em módulos;
* persistência de dados;
* controle de estoque;
* relacionamento entre diferentes conjuntos de dados;
* criação de histórico de movimentações.

## Autor

**Arthur Sousa**

Estudante de Ciência da Computação e interessado em **Engenharia de Dados, Python, SQL, bancos de dados e construção de pipelines de dados**.
