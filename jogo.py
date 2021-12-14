from pessoas import Pessoa
from jogadores import Computador, Humano
from itertools import cycle
from faker import Faker


class Jogo:
    def __init__(self, fake, generos):
        while generos:
            genero = generos.pop()
            if genero == 'F':
                Pessoa(
                    fake.first_name_female()
                ).barba = 'não tem'
            else:
                Pessoa(fake.first_name_male())
        computador, humano = Computador(), Humano()
        computador.adversario = humano
        humano.adversario = computador
        self.sequencia_jogo = cycle([computador, humano])

    def executa(self):
        jogador = next(self.sequencia_jogo)
        jogador.faz_pergunta()
        if len(jogador.suspeitos) == 1:
            print('\nVitória do {}'.format(
                jogador.__class__.__name__
            ))
            return False
        return True


if __name__ == '__main__':
    print('\n', ' JOGO CARA-A-CARA '.center(60, '='), '\n')
    jogo = Jogo(
        fake = Faker('pt_BR'),
        generos = list('MFFMFMMFMMFFMFMFFMMMFMFFMFFMF')
    )
    jogadas = 0
    while jogo.executa():
        jogadas += 1
    print('* * * Fim do jogo em {} jogadas'.format(jogadas))
