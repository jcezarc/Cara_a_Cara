from random import choice


class Pessoa:

    TODOS_ATRIBUTOS = { # Valores possíveis, função para FILTRO e tamanho para exibição
        'cor_cabelo': (['loiro', 'castanho', 'preto'], lambda p, v: p.cor_cabelo == v, 12),
        'tam_cabelo': (['curto', 'médio', 'comprido'], lambda p, v: p.tam_cabelo == v, 20),
        'olhos': (['verdes', 'castanhos', 'pretos'], lambda p, v: p.olhos == v, 12),
        'barba': (['grande', 'curta', 'não tem'], lambda p, v: p.barba == v, 10),
        'oculos': (['fino', 'grosso', 'de sol', 'não tem'], lambda p, v: p.oculos == v, 10),
        'rosto': (['quadrado', 'oval', 'arredondado'], lambda p, v: p.rosto == v, 14)
    }
    lista = []

    def __init__(self, nome, **caracteristicas):
        self.nome = nome
        aleatorio = not caracteristicas
        for atributo, opcoes in Pessoa.TODOS_ATRIBUTOS.items():
            valor_padrao = choice(opcoes[0]) if aleatorio else None
            setattr(self, atributo, caracteristicas.get(atributo, valor_padrao))
        Pessoa.lista.append(self)

    @classmethod
    def filtro(cls, atributo, valor, igual=True, lista=None):
        pergunta = cls.TODOS_ATRIBUTOS[atributo][1]
        return [p for p in (lista or cls.lista) if pergunta(p, valor) == igual]
