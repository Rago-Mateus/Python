start = input(print('Vamos jogar adivinhação? Responda Start para começar.')).lower()
if start == 'start':
    import random
    computador = random.randint(0,5)
    print(10 * '++==')
    jogador = input(print('Em que número o pc pensou?'))
    print(10*'++==')
    if jogador == computador:
        print('Você acertou!')
    else:
        print('Você errou! O computador pensou em {} e vc em {}.'.format(computador,jogador))
else:
    print('Exit, tchau.')



