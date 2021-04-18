print('Programa de ALISTAMENTO MILITAR!!!')

import datetime
ano = int(datetime.date.today().year)

n = str(input('Qual sua data de nascimento? Escreva como XX\XX\XXXX'))
n_y = n[6:11]
n_y = int(n_y)

if ano==n_y+18:
    print('Parabéns, este é o seu ano de alistamento militar.')
elif ano<n_y+18:
    print('Ainda faltam {} anos para seu alistamento militar.'.format(n_y+18-ano))
else:
    print('Já se passou {} anos do ano do seu alistamento militar.'.format((ano-n_y-18)))

print('++FIM++')
