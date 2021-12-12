from pessoas import Pessoa
from random import choice


class Jogador:
    def __init__(self):
        self.suspeitos = Pessoa.lista
        self.personagem = self.escolha(Pessoa.lista, '>> Escolha um personagem **')
        self.adversario = None

    def responde_pergunta(self, atributo, valor):
        return getattr(self.personagem, atributo) == valor

    def faz_pergunta(self):
        atributo = self.escolha(list(Pessoa.TODOS_ATRIBUTOS), 'FAÇA UMA PERGUNTA sobre...')
        valores = Pessoa.TODOS_ATRIBUTOS[atributo][0]
        valor = 'tem' if valores[0] == 'tem' else self.escolha(valores, '...igual a...')
        print('-'*100, '\n')
        resposta = self.adversario.responde_pergunta(atributo, valor)
        self.suspeitos = Pessoa.filtro(atributo, valor, resposta, self.suspeitos)
        print('[{}] -- {}: {}? {}'.format(
            self.__class__.__name__,
            atributo, valor, 'SIM' if resposta else 'NÃO'
        ))
        self.exibe_resultado()


class Computador(Jogador):
    def escolha(self, lista, titulo):
        return choice(lista)

    def exibe_resultado(self):
        print('-'*100)


class Humano(Jogador):
    def escolha(self, lista, titulo):
        print(titulo)
        if lista == self.suspeitos:
            self.exibe_resultado(True)
        else:
            print('\n'.join(f'{i} - {p}' for i, p in enumerate(lista, 1)))
        i = -1
        while not i in range(len(lista)):
            i = int(input(': '))-1
        return lista[i]

    def exibe_resultado(self, com_numeros=False):
        cabecalho = {a: v[-1] for a, v in Pessoa.TODOS_ATRIBUTOS.items()}
        cabecalho['nome'] = 20
        print('\n{}\n{}'.format(
            ' '.join(campo.center(tam)[:tam] for campo, tam in cabecalho.items()),
            '+'.join('-'*tam for campo, tam in cabecalho.items())
        ))
        for i, pessoa in enumerate(self.suspeitos, 1):
            dados = pessoa.__dict__
            linha = '|'.join(dados[campo].center(tam)[:tam] for campo, tam in cabecalho.items())
            if com_numeros:
                linha += f'  => {i}'
            print(linha)

    def responde_pergunta(self, atributo, valor):
        print('Seu personagem: {}'.format(
            str(self.personagem.__dict__)
        ))
        return super().responde_pergunta(atributo, valor)
