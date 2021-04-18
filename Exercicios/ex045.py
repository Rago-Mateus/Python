import random
import time
print('Vamos jogar JOKENPÔ!!!!')
print('====--===='*10)
s = input('===PRESS TO START===')
print('O computador está escolhendo entre Pedra, Papel, Tesoura. Aguarde.')
time.sleep(3)
print('Pronto, o computador já escolheu. Sua vez!')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
p2 = (random.randint(0,2))

time.sleep(1)
p1 = input('Escolha PEDRA, PAPEL ou TESOURA').upper()
print('Vejamos quem ganhou!')
time.sleep(3)

if  p1=='PEDRA' and itens[p2]=='PEDRA' or p1=='PAPEL' and itens[p2]=='PAPEL' or p1=='TESOURA' and itens[p2]=='TESOURA':
    print('O jogo EMPATOU! Você escolheu {} e o computador {}.'.format(p1,itens[p2]))
elif p1=='PEDRA' and itens[p2]=='PAPEL':
    print('O COMPUTADOR GANHOU! Você escolheu {} e o computador {}.'.format(p1, itens[p2]))
elif p1=='PEDRA' and itens[p2]=='TESOURA':
    print('VOCÊ GANHOU! Você escolheu {} e o computador {}.'.format(p1, itens[p2]))
else:
    print('O COMPUTADOR GANHOU! Você escolheu {} e o computador {}.'.format(p1, itens[p2]))

print('====FIM====')

