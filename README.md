# Exercism Python Workspace

Este repositório guarda os exercícios do track Python do Exercism.

## Setup

1. Rode o bootstrap:

```bash
make bootstrap
```

2. Se o Poetry estiver instalado, ele será usado automaticamente. Caso contrário, o Makefile cria e usa `.venv` local.

```bash
poetry shell
```

## Testes

Para rodar tudo a partir da raiz do repositório:

```bash
make test
```

Se preferir chamar o runner diretamente:

```bash
poetry run python runtests.py
```

Se o Poetry não estiver disponível, o equivalente é:

```bash
.venv/bin/python runtests.py
```

Para rodar só um exercício específico:

```bash
make test EX=hello-world
```

Se quiser ver os comandos disponíveis:

```bash
make help
```
