from pessoas import Pessoa
from jogadores import Computador, Humano
from itertools import cycle
from random import shuffle


class Jogo:
    def __init__(self, homens, mulheres):
        personagens = homens + mulheres
        shuffle(personagens)
        while personagens:            
            personagem = personagens.pop()
            Pessoa(personagem).barba = 'tem' if personagem in homens else 'não tem'
        computador, humano = Computador(), Humano()
        computador.adversario = humano
        humano.adversario = computador
        self.sequencia_jogo = cycle([computador, humano])

    def executa(self):
        jogador = next(self.sequencia_jogo)
        jogador.faz_pergunta()
        if len(jogador.suspeitos) == 1:
            print('Vitória do {}'.format(
                jogador.__class__.__name__
            ))
            return False
        return True


if __name__ == '__main__':
    print('\n', 'JOGO CARA-A-CARA'.center(60, '='), '\n')
    jogo = Jogo(
        homens=['João Pedro', 'Isaac', 
        'Yago', 'Murilo', 'Robert'],
        mulheres=['Heloísa', 'Giovanna',
        'Kamilly', 'Agatha', 'Isadora']
    )
    jogadas = 0
    while jogo.executa():
        jogadas += 1
    print('* * * Fim do jogo em {} jogadas'.format(jogadas))
