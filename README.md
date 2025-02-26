# python-exercism

Este repositório contém os exercícios e aulas do [Exercism.org](https://exercism.org/) para a linguagem Python.

## 🚀 Configurando o ambiente

Este projeto utiliza **virtualenv** para gerenciar dependências junto com **Poetry** para controle de pacotes. Siga os passos abaixo para configurar o ambiente corretamente.

### 1️⃣ Instalar o virtualenv e o Poetry
Se ainda não tem o virtualenv e o Poetry instalados, execute:
```sh
pip install virtualenv
pip install poetry
```

Ou instale o Poetry via **curl**:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### 2️⃣ Clonar o repositório
```sh
git clone https://github.com/seu-usuario/python-exercism.git
cd python-exercism
```

### 3️⃣ Criar e ativar o ambiente virtual
```sh
python -m venv venv  # Criar o ambiente virtual
source venv/bin/activate  # Ativar no macOS/Linux
venv\Scripts\activate  # Ativar no Windows
```

### 4️⃣ Instalar as dependências
```sh
poetry install
```
Isso instalará todas as dependências definidas no `pyproject.toml`.

## 🎯 Executando os Exercícios
Para rodar um arquivo Python específico:
```sh
poetry run python nome_do_arquivo.py
```

Para rodar os testes (caso existam):
```sh
poetry run pytest
```

## 🛠️ Adicionando Novas Dependências
Para adicionar uma nova dependência ao projeto:
```sh
poetry add nome-do-pacote
```
Se for uma dependência apenas para desenvolvimento:
```sh
poetry add --dev nome-do-pacote
```

## 🧹 Atualizando Dependências
Para atualizar todas as dependências do projeto:
```sh
poetry update
```

---
Agora você está pronto para praticar Python com os exercícios do Exercism! 🚀🐍
