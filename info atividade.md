# Entrega da Atividade - TDD

## 1. Cenário escolhido

O cenário escolhido foi o **Sistema de Gerenciamento de Notas**, apresentado no arquivo `Cenários.pdf`.

## 2. Objetivo do sistema

O sistema permite cadastrar notas de um aluno, validar se as notas estão dentro do intervalo aceito, calcular a média e verificar a situação final do aluno.

## 3. Regras de negócio implementadas

- A nota deve ser numérica.
- A nota deve estar entre 0 e 10.
- Média maior ou igual a 7: aluno aprovado.
- Média entre 5 e 6.9: aluno em recuperação.
- Média menor que 5: aluno reprovado.
- Quando não existem notas cadastradas, a média retorna 0.

## 4. Aplicação do ciclo TDD

### RED

Primeiro foram criados testes unitários para descrever o comportamento esperado do sistema. Exemplos:

- cadastrar nota válida;
- rejeitar nota menor que 0 ou maior que 10;
- rejeitar valores que não são números;
- calcular a média corretamente;
- verificar aprovação, recuperação e reprovação.

Nessa etapa, os testes representam as regras antes da implementação completa.

### GREEN

Depois foi implementada a classe `GerenciamentoNotas` com o mínimo necessário para os testes passarem:

- `adicionar_nota`;
- `cadastrar_notas`;
- `calcular_media`;
- `verificar_situacao`.

### REFACTOR

Por fim, o código foi melhorado sem alterar o comportamento validado pelos testes:

- uso de constantes para limites e médias;
- separação da validação em `_validar_nota`;
- correção da acentuação dos textos;
- melhoria dos testes com `parametrize` para cobrir mais casos.

## 5. Arquivos do projeto

- `gerenciamento_notas.py`: classe principal com as regras do sistema.
- `test_gerenciamento_notas.py`: testes unitários com pytest.
- `README.md`: documentação para execução e entendimento do projeto.
- `requirements.txt`: dependências necessárias.
- `reports/pytest_output.txt`: evidência da execução dos testes no terminal.
- `reports/pytest_report.xml`: relatório JUnit XML gerado pelo pytest.
- `reports/pytest_report.html`: relatório HTML simples gerado a partir do resultado dos testes.

## 6. Evidência de execução

Comando utilizado:

```bash
python -m pytest -v --junitxml=reports/pytest_report.xml
```

Resultado validado:

```text
16 passed
```

## 7. Conclusão

A atividade atende aos requisitos dos PDFs: utiliza Python, pytest, testes unitários, ciclo RED -> GREEN -> REFACTOR, classe implementada, validação das regras de negócio e evidências de execução dos testes.
