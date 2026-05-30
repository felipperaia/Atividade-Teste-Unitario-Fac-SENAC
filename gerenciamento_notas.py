class GerenciamentoNotas:
    """Sistema simples para cadastrar notas e avaliar a situação do aluno."""

    NOTA_MINIMA = 0
    NOTA_MAXIMA = 10
    MEDIA_APROVACAO = 7
    MEDIA_RECUPERACAO = 5

    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        nota_validada = self._validar_nota(nota)
        self.notas.append(nota_validada)

    def cadastrar_notas(self, notas):
        for nota in notas:
            self.adicionar_nota(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()

        if media >= self.MEDIA_APROVACAO:
            return "aprovado"
        if media >= self.MEDIA_RECUPERACAO:
            return "recuperação"
        return "reprovado"

    def _validar_nota(self, nota):
        if isinstance(nota, bool) or not isinstance(nota, (int, float)):
            raise TypeError("A nota precisa ser um número.")

        if nota < self.NOTA_MINIMA or nota > self.NOTA_MAXIMA:
            raise ValueError("A nota deve estar entre 0 e 10.")

        return float(nota)
