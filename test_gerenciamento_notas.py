import pytest

from gerenciamento_notas import GerenciamentoNotas


def test_adicionar_nota_valida():
    sistema = GerenciamentoNotas()

    sistema.adicionar_nota(8)

    assert sistema.notas == [8.0]


def test_cadastrar_varias_notas():
    sistema = GerenciamentoNotas()

    sistema.cadastrar_notas([6, 7.5, 9])

    assert sistema.notas == [6.0, 7.5, 9.0]


@pytest.mark.parametrize("nota_invalida", [-1, 10.1, 11])
def test_adicionar_nota_fora_do_intervalo(nota_invalida):
    sistema = GerenciamentoNotas()

    with pytest.raises(ValueError, match="A nota deve estar entre 0 e 10."):
        sistema.adicionar_nota(nota_invalida)


@pytest.mark.parametrize("nota_invalida", ["dez", None, True])
def test_adicionar_nota_com_tipo_invalido(nota_invalida):
    sistema = GerenciamentoNotas()

    with pytest.raises(TypeError, match="A nota precisa ser um número."):
        sistema.adicionar_nota(nota_invalida)


def test_calcular_media_correta():
    sistema = GerenciamentoNotas()
    sistema.cadastrar_notas([6, 8, 10])

    assert sistema.calcular_media() == pytest.approx(8.0)


def test_calcular_media_sem_notas_retorna_zero():
    sistema = GerenciamentoNotas()

    assert sistema.calcular_media() == 0


@pytest.mark.parametrize(
    ("notas", "situacao"),
    [
        ([7, 7], "aprovado"),
        ([5, 6.9], "recuperação"),
        ([0, 4.9], "reprovado"),
    ],
    ids=["aprovado", "recuperacao", "reprovado"],
)
def test_verificar_situacao_do_aluno(notas, situacao):
    sistema = GerenciamentoNotas()
    sistema.cadastrar_notas(notas)

    assert sistema.verificar_situacao() == situacao


@pytest.mark.parametrize(
    ("notas", "situacao"),
    [
        ([7], "aprovado"),
        ([5], "recuperação"),
        ([4.99], "reprovado"),
    ],
    ids=["limite_aprovado", "limite_recuperacao", "limite_reprovado"],
)
def test_verificar_situacao_nos_limites(notas, situacao):
    sistema = GerenciamentoNotas()
    sistema.cadastrar_notas(notas)

    assert sistema.verificar_situacao() == situacao
