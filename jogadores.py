from pessoas import Pessoa
from random import choice


class Jogador:
    def __init__(self):
        self.suspeitos = Pessoa.lista
        self.personagem = self.escolha(Pessoa.lista, '>> Escolha um personagem')
        self.adversario = None
        self.perguntas = None

    def responde_pergunta(self, atributo, valor):
        return getattr(self.personagem, atributo) == valor

    def faz_pergunta(self):
        self.perguntas = Pessoa.resumo(self.suspeitos)
        atributo = self.escolha(list(self.perguntas), 'FAÇA UMA PERGUNTA sobre...')
        valor = self.escolha(self.perguntas[atributo], '...igual a...')
        print('='*100, '\n')
        resposta = self.adversario.responde_pergunta(atributo, valor)
        self.suspeitos = Pessoa.filtro(atributo, valor, resposta, self.suspeitos)        
        if valor == 'não tem':
            resposta = not resposta
            atributo, valor = 'tem', atributo
        print('[{}] -- {} {}? {}'.format(
            self.__class__.__name__,
            atributo, valor, 'SIM' if resposta else 'NÃO'
        ))
        self.exibe_resultado()


class Computador(Jogador):
    def escolha(self, lista, titulo):
        return choice(lista)

    def exibe_resultado(self):
        print('\t{} restantes\n'.format(len(self.suspeitos)), '-'*100)


class Humano(Jogador):
    def escolha(self, lista, titulo):
        print(titulo)
        if lista == self.suspeitos:
            self.exibe_resultado()
        else:
            print('\n'.join(f'{i} - {p}' for i, p in enumerate(lista)))
        i = -1
        while not i in range(len(lista)):
            try:
                i = int(input(': '))
            except ValueError:
                print(titulo)
        return lista[i]

    def exibe_resultado(self):
        print(Pessoa.grade(self.suspeitos))

    def responde_pergunta(self, atributo, valor):
        print('Seu personagem: {}'.format(
            str(self.personagem.__dict__)
        ))
        return super().responde_pergunta(atributo, valor)
