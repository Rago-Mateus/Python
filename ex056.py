media = 0
idade = 0
velho = 0
mulheres = 0
idoso = 'nome'
for c in range(1,4):
    nome = str(input('Qual o nome da {} pessoa?'.format(c)))
    idade = int(input('Qual a idade da {} pessoa?'.format(c)))
    if idade >= velho:
        velho = idade
        idoso = nome
    media = idade + media
    sexo = input('Qual o sexo da {} pessoa? escreva masculino ou feminino'.format(c))
    if sexo == 'feminino':
        mulheres = mulheres +1
media = media / 3
print('A média de idade entre as pessoas é {}'.format(media))
print('A pessoa mais velha é chama-se {}'.format(idoso))
print('A quantidade de mulheres é {}.'.format(mulheres))