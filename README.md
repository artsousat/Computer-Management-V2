# Computer Management — V2

Sistema de gerenciamento de equipamentos desenvolvido em Python, criado para evoluir um projeto de controle de empréstimos em direção a uma aplicação mais estruturada e orientada a dados.

A **V2** tem como principal objetivo introduzir **persistência de dados**, organização do código em módulos e uma estrutura preparada para futuras evoluções com **SQLite, SQL, histórico de movimentações e métricas**.

> **Status:** 🚧 Em desenvolvimento — V2

---

## 🎯 Objetivo do projeto

O Computer Management foi pensado para representar um cenário real de controle de equipamentos em uma escola.

O sistema deverá permitir:

- cadastrar e gerenciar professores;
- cadastrar e gerenciar dispositivos;
- controlar o estoque disponível;
- registrar empréstimos;
- registrar devoluções;
- manter histórico das movimentações;
- armazenar os dados de forma persistente;
- futuramente transformar os dados gerados pelo sistema em informações úteis para análise.

A V2 é uma etapa intermediária entre um programa totalmente baseado em memória e uma aplicação orientada a banco de dados.

---

## 🏗️ Estrutura atual

```text
Computer Management-V2/
│
├── dados/
│   └── professores.json
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

### `main.py`

É o ponto de entrada da aplicação.

Responsabilidades atuais:

- iniciar o sistema;
- exibir o menu principal;
- direcionar o usuário para os módulos de professores, dispositivos e empréstimos;
- tratar entradas inválidas no menu principal.

### `src/professores.py`

Responsável pelo gerenciamento dos professores.

Atualmente possui:

- carregamento dos professores;
- cadastro de novos professores;
- visualização dos professores;
- remoção de professores;
- persistência dos dados em JSON;
- menu específico de professores.

### `src/dispositivos.py`

Módulo destinado ao gerenciamento dos equipamentos.

O menu já está estruturado e preparado para receber as funcionalidades de:

- cadastro;
- visualização;
- remoção;
- controle de estoque.

As operações ainda estão em desenvolvimento.

### `src/emprestimos.py`

Módulo destinado ao controle dos empréstimos.

O menu já está estruturado para:

- realizar empréstimos;
- visualizar dispositivos em uso;
- realizar devoluções;
- consultar histórico;
- limpar o histórico do dia.

As operações ainda estão em desenvolvimento.

### `src/utils.py`

Contém funções reutilizáveis pelo sistema.

Atualmente possui a função responsável pelo cabeçalho dos menus, incluindo:

- título da tela;
- data atual;
- horário atual.

### `dados/professores.json`

Arquivo utilizado como primeira camada de persistência da V2.

Os professores cadastrados deixam de existir apenas durante a execução do programa e passam a ser armazenados em um arquivo JSON.

---

## 💾 Persistência de dados

Uma das principais mudanças da V1 para a V2 é a introdução de **persistência**.

Na V1, os dados existiam apenas enquanto o programa estava executando.

Na V2, os professores são armazenados em:

```text
dados/professores.json
```

O sistema utiliza o módulo `json` do Python para:

1. abrir o arquivo;
2. carregar os dados;
3. transformar o JSON em um dicionário Python;
4. modificar os dados;
5. salvar novamente o dicionário no arquivo.

Essa estrutura prepara o projeto para uma próxima evolução: substituir o armazenamento em arquivos por um **banco de dados relacional**.

---

## 🧩 Organização modular

A V2 também representa uma evolução na arquitetura do código.

Em vez de concentrar todas as funções em um único arquivo, o projeto foi dividido por responsabilidade:

```text
main.py
   │
   ├── professores.py
   ├── dispositivos.py
   ├── emprestimos.py
   └── utils.py
```

Essa separação facilita:

- manutenção;
- leitura do código;
- localização de funcionalidades;
- testes;
- evolução independente dos módulos;
- futura integração com banco de dados.

---

## 🛠️ Tecnologias e conceitos utilizados

### Linguagem

- Python 3

### Bibliotecas

- `json`
- `os`
- `time`
- `datetime`

### Conceitos praticados

- funções;
- módulos e imports;
- dicionários;
- listas;
- estruturas condicionais;
- loops `while`;
- tratamento de exceções com `try/except`;
- leitura e escrita de arquivos;
- persistência em JSON;
- separação de responsabilidades;
- organização de projeto em diretórios.

---

## ▶️ Como executar

Com o Python instalado, abra um terminal na pasta raiz do projeto:

```bash
python main.py
```

O sistema iniciará o menu principal:

```text
========================================
           COMPUTER MANAGEMENT
           DD/MM/AA - HH:MM:SS
========================================

[1] Professores
[2] Dispositivos
[3] Empréstimos
[0] Sair
```

---

## 📌 Funcionalidades

### ✅ Implementadas

- [x] Menu principal
- [x] Menu de professores
- [x] Cadastro de professores
- [x] Visualização de professores
- [x] Remoção de professores
- [x] Persistência de professores em JSON
- [x] Geração automática do próximo identificador de professor
- [x] Cabeçalho com data e horário
- [x] Tratamento de entradas inválidas nos menus

### 🚧 Em desenvolvimento

- [ ] Cadastro de dispositivos
- [ ] Visualização de dispositivos
- [ ] Remoção de dispositivos
- [ ] Controle de estoque
- [ ] Registro de empréstimos
- [ ] Controle de dispositivos em uso
- [ ] Devolução parcial
- [ ] Devolução total
- [ ] Histórico de empréstimos
- [ ] Registro de data e horário das movimentações
- [ ] Limpeza do histórico diário
- [ ] Persistência dos demais dados

---

## 🗺️ Roadmap

A evolução planejada do projeto segue aproximadamente esta sequência:

### V2 — Persistência e organização

- organização do código em módulos;
- persistência em JSON;
- separação dos menus por responsabilidade;
- gerenciamento de professores, dispositivos e empréstimos.

### V3 — Banco de dados

- introdução do SQLite;
- modelagem das tabelas;
- criação de relacionamentos;
- operações CRUD utilizando SQL;
- substituição gradual dos arquivos JSON pelo banco.

### V4 — Histórico e dados

- histórico completo de empréstimos;
- registro de devoluções;
- identificação de responsáveis;
- consultas SQL;
- métricas de utilização dos equipamentos.

### V5 — Engenharia de Dados

Evolução do sistema para gerar um fluxo de dados mais próximo de um projeto de Engenharia de Dados:

```text
Sistema
   ↓
Dados transacionais
   ↓
Extração
   ↓
Transformação
   ↓
Carga
   ↓
Banco de dados
   ↓
Consultas / Métricas
   ↓
Análise
```

Possíveis métricas:

- quantidade de empréstimos;
- equipamentos mais utilizados;
- professores com maior número de empréstimos;
- quantidade de devoluções;
- utilização dos equipamentos ao longo do tempo;
- disponibilidade do estoque;
- frequência de utilização por tipo de dispositivo.

---

## 📚 O que este projeto demonstra

Mais do que um sistema de menus, o projeto está sendo utilizado como uma forma prática de estudar a evolução de uma aplicação:

**V1**

```text
Python
↓
Lógica
↓
Dados em memória
```

**V2**

```text
Python
↓
Organização modular
↓
Persistência
↓
JSON
```

**Próximas versões**

```text
Python
↓
Banco de dados
↓
SQL
↓
Modelagem
↓
Histórico
↓
ETL
↓
Métricas
```

Essa evolução permite praticar conceitos de desenvolvimento de software enquanto aproxima o projeto de problemas encontrados em sistemas orientados a dados.

---

## 👨‍💻 Projeto de estudo

Projeto desenvolvido como parte da formação prática em **Ciência da Computação**, com foco em Python, bancos de dados, SQL e Engenharia de Dados.

O projeto será evoluído progressivamente, mantendo versões anteriores como etapas do processo de aprendizagem.
