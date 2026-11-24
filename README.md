# 🎬 Gerenciador de Filmes em Python

## 📖 Sobre o projeto

O Gerenciador de Filmes é uma aplicação desenvolvida em Python que permite cadastrar, listar, pesquisar, remover e substituir filmes por meio de um menu interativo no terminal. Também é possível consultar a quantidade de filmes cadastrados.

O projeto tem finalidade educacional e demonstra a aplicação prática de conceitos fundamentais de lógica de programação, estruturas condicionais, estruturas de repetição e manipulação de listas em Python.

## 🚀 Funcionalidades

| Opção | Funcionalidade | Descrição |
| :---: | --- | --- |
| 1 | Listar | Exibe todos os filmes cadastrados ou informa que a lista está vazia. |
| 2 | Adicionar | Adiciona um novo filme ao final da lista. |
| 3 | Pesquisar | Consulta um filme por sua posição na lista. |
| 4 | Remover | Remove um filme por sua posição na lista. |
| 5 | Quantidade de Filmes | Exibe o total de filmes cadastrados. |
| 6 | Substituir | Altera o nome de um filme já cadastrado. |
| 7 | Sair | Encerra a execução do programa. |

## 🛠️ Tecnologias utilizadas

- Python 3
- Terminal ou console
- Biblioteca padrão do Python, sem necessidade de instalar dependências externas.

## ▶️ Como executar o projeto

### Pré-requisitos

Ter o [Python 3](https://www.python.org/downloads/) instalado no computador.

### Passo a passo

1. Salve o código-fonte em um arquivo chamado `main.py`.
2. Abra o terminal na pasta em que o arquivo foi salvo.
3. Execute o comando:

```bash
python main.py
```

Caso o comando `python` não esteja disponível, utilize:

```bash
python3 main.py
```

4. Escolha uma das opções exibidas no menu.

## 💻 Menu principal

```text
1) Listar
2) Adicionar
3) Pesquisar
4) Remover
5) Quantidade de Filmes
6) Substituir
7) Sair
Digite a sua opção:
```

O menu é apresentado continuamente até que o usuário escolha a opção 7.

## ⚙️ Como o programa funciona

### 1. Armazenamento dos filmes

Os nomes dos filmes são armazenados em uma lista, inicialmente vazia:

```python
filmes = []
```

A lista permanece na memória durante a execução do programa.

### 2. Estrutura de repetição

O comando `while True` mantém o menu em execução. A instrução `break` interrompe o laço quando o usuário escolhe sair.

### 3. Estruturas condicionais

As instruções `if`, `elif` e `else` são utilizadas para identificar a opção selecionada e executar a funcionalidade correspondente.

### 4. Manipulação da lista

| Recurso | Finalidade |
| --- | --- |
| `filmes.append(novo_filme)` | Adiciona um filme. |
| `filmes[codigo - 1]` | Acessa um filme pela sua posição. |
| `filmes.pop(codigo - 1)` | Remove um filme. |
| `len(filmes)` | Retorna a quantidade de filmes. |
| `filmes[codigo - 1] = nome_novo_filme` | Substitui um filme. |
| `for item in filmes` | Percorre a lista para exibir os filmes. |

### 5. Validação dos códigos

O programa verifica se o código informado corresponde a uma posição válida na lista:

```python
if codigo >= 1 and codigo <= len(filmes):
```

O usuário informa posições a partir de 1, enquanto os índices das listas em Python começam em 0. Por esse motivo, o programa utiliza `codigo - 1` para acessar os elementos.

| Código informado | Índice em Python | Filme |
| :---: | :---: | --- |
| 1 | 0 | Interestelar |
| 2 | 1 | Matrix |
| 3 | 2 | Avatar |

Os códigos representam posições, e não identificadores permanentes. Ao remover um filme, as posições dos filmes seguintes são alteradas.

## 📝 Exemplo de utilização

Exemplo de interação, com as repetições do menu omitidas para facilitar a leitura:

```text
Digite a sua opção: 2
Informe o nome do novo filme: Interestelar
Filme adicionado com sucesso!

Digite a sua opção: 2
Informe o nome do novo filme: Matrix
Filme adicionado com sucesso!

Digite a sua opção: 1
Lista de Filmes
- Interestelar
- Matrix

Digite a sua opção: 3
Informe a codigo do filme: 2
O filme pesquisado foi Matrix

Digite a sua opção: 5
Atualmente tem(os) 2 filme(s)

Digite a sua opção: 7
Obrigado
```

## 📚 Conceitos de programação abordados

- Variáveis e tipos de dados (`int` e `str`).
- Entrada e saída de dados (`input()` e `print()`).
- Listas, índices e métodos de manipulação.
- Estruturas condicionais (`if`, `elif` e `else`).
- Estruturas de repetição (`while` e `for`).
- Operadores relacionais e lógicos.
- Validação de posições e controle do fluxo de execução.
- Operações básicas de CRUD: Create (criar), Read (consultar), Update (atualizar) e Delete (remover).

## 📁 Estrutura sugerida do projeto

```text
gerenciador-filmes/
├── main.py       # Código-fonte da aplicação
└── README.md     # Documentação do projeto
```

## 🔮 Possíveis melhorias

- Exibir os códigos dos filmes junto aos seus nomes na listagem.
- Permitir a pesquisa pelo nome do filme.
- Impedir o cadastro de nomes vazios ou duplicados.
- Tratar entradas não numéricas utilizando `try` e `except`, evitando erros de execução.
- Organizar o código em funções.
- Adicionar informações como gênero, ano de lançamento e avaliação.
- Salvar os filmes em um arquivo JSON ou banco de dados.
- Criar uma interface gráfica ou web.

## ⚠️ Limitações da versão atual

Os filmes são armazenados apenas na memória e são perdidos quando o programa é encerrado. A pesquisa é realizada pela posição do filme, e não pelo nome. Além disso, entradas não numéricas nos campos de opção ou código podem causar um erro `ValueError`, pois ainda não há tratamento de exceções.

---

Projeto desenvolvido para fins de aprendizagem e prática de programação em Python.
