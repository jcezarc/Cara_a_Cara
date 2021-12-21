from random import choice
from collections import Counter


FILTER_FUNCTIONS = {
    True: lambda p, a, v: getattr(p, a) == v,
    False: lambda p, a, v: getattr(p, a) != v,
}
MAIS_COMUM = 0
MENOS_COMUM = -1

class Pessoa:

    TODOS_ATRIBUTOS = { # Valores possíveis e tamanho para exibição
        'cor_cabelo': (['loiro', 'castanho', 'preto', 'ruivo'], 12),
        'tam_cabelo': (['curto', 'médio', 'comprido'], 20),
        'olhos': (['verdes', 'castanhos', 'pretos', 'azuis'], 12),
        'barba': (['grande', 'curta', 'não tem'], 10),
        'oculos': (['finos', 'grossos', 'de sol', 'não tem'], 10),
        'rosto': (['quadrado', 'oval', 'arredondado', 'triangular'], 14)
    }
    lista = []
    selecionada = None

    def __init__(self, nome, **caracteristicas):
        self.nome = nome
        aleatorio = not caracteristicas
        for atributo, opcoes in Pessoa.TODOS_ATRIBUTOS.items():
            valor_padrao = choice(opcoes[0]) if aleatorio else None
            setattr(self, atributo, caracteristicas.get(atributo, valor_padrao))
        Pessoa.lista.append(self)

    @classmethod
    def filtro(cls, atributo, valor, lista=None, func=FILTER_FUNCTIONS[True]):
        return [p for p in (lista or cls.lista) if func(p, atributo, valor)]

    @classmethod
    def seleciona(cls, nivel):
        lista = cls.lista
        for a, v in cls.resumo(lista).items():
            dados = cls.filtro(a, v[nivel], lista)
            if not dados:
                break
            lista = dados
        cls.selecionada = lista[0]

    @staticmethod
    def resumo(lista):
        R = {a: Counter([p.__dict__[a] for p in lista]).most_common() for a in Pessoa.TODOS_ATRIBUTOS}
        return {k: [n for n, v in e] for k, e in R.items() if len(e) > 1}
    
    @staticmethod
    def grade(lista):
        if isinstance(lista[0], str):
            return '\n'.join(f'{i} - {p}' for i, p in enumerate(lista))
        head = {**{a: v[-1] for a, v in Pessoa.TODOS_ATRIBUTOS.items()}, **{'nome': 20}}
        return '\n{}\n{}\n'.format(
            ' '.join(c.center(v)[:v] for c, v in head.items()),
            '+'.join('-'*v for c, v in head.items())
        ) + '\n'.join(
            '|'.join(p.__dict__[c].center(v)[:v] for c, v in head.items()) + '{} {}'.format(
                i, '<<' if p == Pessoa.selecionada else ''
            )            
            for i, p in enumerate(lista)
        )
