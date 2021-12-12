from random import choice


class Pessoa:

    TODOS_ATRIBUTOS = { # Valores possíveis, função para FILTRO e tamanho para exibição
        'cor_cabelo': (['loiro', 'castanho'], lambda p, v: p.cor_cabelo == v, 12),
        'cabelo_comprido': (['tem', 'não tem'], lambda p, v: p.cabelo_comprido == v, 20),
        'olhos': (['verdes', 'castanhos'], lambda p, v: p.olhos == v, 12),
        'barba': (['tem', 'não tem'], lambda p, v: p.barba == v, 10),
        'oculos': (['tem', 'não tem'], lambda p, v: p.oculos == v, 10),
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
