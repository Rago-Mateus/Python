print('Bem vindo à calculadora de preços de viagens')
print(('--==--')*15)
d = int(input(print('Qual a distância da sua viagem em km?')))
if d<=200:
    m = d*0.5
else:
    m = d*0.45
print('O preço de sua passagem para a distândia de {}Km é de R${}!'.format(d,m))

print('==FIM==')