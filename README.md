# Atividade Teste Unitário Fac SENAC

Projeto desenvolvido para a atividade de **Test-Driven Development (TDD)** com testes unitários em Python e pytest.

## Cenário

O cenário escolhido foi o **Sistema de Gerenciamento de Notas**.

Funcionalidades implementadas:

- cadastrar notas;
- validar notas inválidas;
- calcular a média;
- verificar a situação do aluno.

## Regras

- Notas válidas devem estar entre 0 e 10.
- Valores não numéricos não são aceitos.
- Média maior ou igual a 7: `aprovado`.
- Média entre 5 e 6.9: `recuperação`.
- Média menor que 5: `reprovado`.

## Estrutura

```text
.
├── gerenciamento_notas.py
├── test_gerenciamento_notas.py
├── info atividade.md
├── requirements.txt
├── README.md
├── .gitignore
└── reports/
    ├── pytest_output.txt
    ├── pytest_report.html
    └── pytest_report.xml
```

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute os testes:

```bash
python -m pytest -v
```

Para gerar o relatório XML:

```bash
python -m pytest -v --junitxml=reports/pytest_report.xml
```

## TDD

O projeto foi organizado seguindo o ciclo **RED -> GREEN -> REFACTOR**:

- **RED**: criação dos testes antes da implementação completa.
- **GREEN**: implementação mínima para os testes passarem.
- **REFACTOR**: melhoria do código mantendo os testes passando.

Mais detalhes estão no arquivo `info atividade.md`.
