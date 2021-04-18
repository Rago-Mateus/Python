resultado = 'inicio'
import random
import time
computador = int(random.randint(1, 10))
erro = 0
print('Vamos jogar adivinhação? O computador irá pensar em um número entre 1 e 10.')
time.sleep(1)
print(10 * '++==')
jogador = int(input('Em que número o pc pensou?'))
print(10*'++==')
time.sleep(1)
while resultado not in 'vitória':
    if jogador - computador == 0:
        resultado = 'vitória'
    else:
        erro = erro+1
        resultado = 'derrota'
        time.sleep(1)
        jogador = int(input('Você errou! O computador não pensou em {}. Tente novamente:'.format(jogador)))
time.sleep(1)
print('Sim! Você acertou, parabéns! O computador pensou em {}.'.format(computador))
print('Você tentou {} vezes antes de conseguir acertar!'.format(erro+1))