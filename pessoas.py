from random import choice


class Pessoa:

    TODOS_ATRIBUTOS = { # Valores possíveis, função para FILTRO e tamanho para exibição
        'cor_cabelo': (['loiro', 'castanho', 'preto'], lambda p, v: p.cor_cabelo == v, 12),
        'tam_cabelo': (['curto', 'médio', 'comprido'], lambda p, v: p.tam_cabelo == v, 20),
        'olhos': (['verdes', 'castanhos', 'pretos'], lambda p, v: p.olhos == v, 12),
        'barba': (['grande', 'curta', 'não tem'], lambda p, v: p.barba == v, 10),
        'oculos': (['finos', 'grossos', 'de sol', 'não tem'], lambda p, v: p.oculos == v, 10),
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

    @staticmethod
    def resumo(lista, tamanho_minimo=2):
        R = {a: list(set([p.__dict__[a] for p in lista])) for a in Pessoa.TODOS_ATRIBUTOS}
        return {k: v for k, v in R.items() if len(v) >= tamanho_minimo}
    
    @staticmethod
    def grade(lista):
        if isinstance(lista[0], str):
            return '\n'.join(f'{i} - {p}' for i, p in enumerate(lista))
        head = {**{a: v[-1] for a, v in Pessoa.TODOS_ATRIBUTOS.items()}, **{'nome': 20}}
        return '\n{}\n{}\n'.format(
            ' '.join(c.center(v)[:v] for c, v in head.items()),
            '+'.join('-'*v for c, v in head.items())
        ) + '\n'.join(
            '|'.join(p.__dict__[c].center(v)[:v] for c, v in head.items()) + f': {i}'
            for i, p in enumerate(lista)
        )
