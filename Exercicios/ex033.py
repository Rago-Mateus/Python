print('Bem vindo a calculadora de vencedores e perdedores')
print(str('==--==')*15)

p1 = input(print('Diga a posição de um jogador.'))
p2 = input(print('Diga a posição de outro jogador.'))
p3 = input(print('E diga a posição de mais um jogador.'))

lista = [p1,p2,p3]
max = max(lista)
min = min(lista)

print('O primeiro colocado é {}'.format(max))
print('O último colocado é o {}'.format(min))

print('==FIM==')
