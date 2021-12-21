from pessoas import Pessoa, FILTER_FUNCTIONS
from random import choice


class Jogador:
    def __init__(self):
        self.suspeitos = Pessoa.lista
        self.personagem = self.escolha(Pessoa.lista, '>> Escolha um personagem:')
        self.adversario = None

    def responde_pergunta(self, atributo, valor):
        return FILTER_FUNCTIONS[True](self.personagem, atributo, valor)

    def faz_pergunta(self):
        perguntas = Pessoa.resumo(self.suspeitos)
        atributo = self.escolha(list(perguntas), 'FAÇA UMA PERGUNTA sobre...')
        valor = self.escolha(perguntas[atributo], '...igual a...')
        print('='*100, '\n')
        resposta = self.adversario.responde_pergunta(atributo, valor)
        self.suspeitos = Pessoa.filtro(atributo, valor, self.suspeitos, FILTER_FUNCTIONS[resposta])        
        if valor == 'não tem':
            resposta = not resposta
            atributo, valor = 'tem', atributo
        print('[{}] -- {} {}? {}'.format(
            self.__class__.__name__,
            atributo, valor, 'SIM' if resposta else 'NÃO'
        ))
        self.exibe_resultado()


class Computador(Jogador):
    def escolha(self, opcoes, mensagem):
        try:
            return choice(opcoes)
        except IndexError:
            print('\nOpções para {}: {}\n'.format(mensagem, opcoes))

    def exibe_resultado(self):
        print('\t{} restantes\n'.format(len(self.suspeitos)), '-'*100)


class Humano(Jogador):
    def escolha(self, opcoes, mensagem):
        print(Pessoa.grade(opcoes))
        i = -1
        while not i in range(len(opcoes)):
            try: i = int(input(mensagem))
            except ValueError: print('Tente novamente')
        return opcoes[i]

    def exibe_resultado(self):
        print(Pessoa.grade(self.suspeitos))

    def responde_pergunta(self, atributo, valor):
        print('Seu personagem: {}'.format(
            str(self.personagem.__dict__)
        ))
        return super().responde_pergunta(atributo, valor)
